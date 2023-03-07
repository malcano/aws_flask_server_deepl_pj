from flask import Flask, render_template, request, redirect, url_for, jsonify, g
from flask_assets import Environment, Bundle
import config
import time
import model, getFlower, create_id

md = model.model()
print("create model instance!")
getflower = getFlower.getFlower()
print("create getflower instance!")

app = Flask(__name__)

assets = Environment(app)

# index page에 scss 적용
index_bundle = Bundle('scss/index.scss', filters='pyscss', output='css/index.css')

app.secret_key = 'dsaklfjiodsjfioasdjfioajdsiofjaiosdj'
# we can use cur like below codes
# cur.execute("쿼리문")
# cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
# conn.commit()

@app.before_request
def before_request():
    g.start_time = time.time() # 요청 시작 시간 저장
    if request.path.startswith('/result'): # 요청이 결과 페이지인 경우에만 로딩 페이지 렌더링
        return render_template('loading.html')

@app.after_request
def after_request(response):
    if request.path.startswith('/result'): # 요청이 결과 페이지인 경우에만 처리
        # 로딩 페이지를 최소 2초 이상 보여주기 위해, 요청이 완료되기 전에 일정 시간이 지나면 기다리지 않고 바로 응답을 보내줌
        response.headers['Refresh'] = '2;url=%s' % request.path
        elapsed_time = time.time() - g.start_time # 요청 처리 시간 측정
        if elapsed_time < 2: # 요청 처리 시간이 2초 미만이면 추가적으로 대기
            time.sleep(2 - elapsed_time)

    return response

@app.route("/")
def kkot():

    return render_template("index.html", css=index_bundle)

@app.route('/result/<input>')
def result(input):#input: 사용자로부터 받는 메세지

    def deeplearning(input):
        sentiment = int(md.sentiment_predict(input))
        circumstance = int(md.circumstance_predict(input))
        return sentiment, circumstance

    id = create_id.id()
    cur = config.conn.cursor()

    #need to insert to Database
    sentence = input
    sentiment, circumstance = deeplearning(sentence)
    rec_flower = getflower.fromFlowerList(sentiment, circumstance) # return value would be like {"flower1":"sentence","flower2":"sentence}
    user_id = id.newID()
    del id
    #need to parse to select_page.html


    first_flower = list(rec_flower.keys())[0]
    second_flower = list(rec_flower.keys())[1]
    first_flower_explain = list(rec_flower.values())[0]
    second_flower_explain = list(rec_flower.values())[1]
    print(f"user id: {user_id} sentence: {sentence} sentiment: {sentiment} circumstance: {circumstance}")
    cur.execute("INSERT INTO flower_result (id,sentence,emotion,situation) VALUES (%s,%s,%s,%s)", (str(user_id),sentence,sentiment,circumstance))
    config.conn.commit()
    cur.close()

    #need to parse img link
    return render_template("select_page.html", \
                           first_flower = first_flower, \
                           second_flower = second_flower, \
                           first_flower_explain = first_flower_explain, \
                           second_flower_explain = second_flower_explain,\
                           user_id = str(user_id))
@app.route('/finalfisrt/<input>')
def finalfirst(input):
    cur = config.conn.cursor()

    get_emotion_SQL = 'SELECT emotion FROM flower_result WHERE id = %s'
    get_situation_SQL = 'SELECT situation FROM flower_result WHERE id = %s'
    cur.execute(get_emotion_SQL, input)
    emotion = cur.fetchall()[0][0]
    print(f"emotion:{emotion}")
    cur.execute(get_situation_SQL, input)
    situation = cur.fetchall()[0][0]
    print(f"emotion:{situation}")
    chosen_flower = getflower.fromFlowerList(emotion,situation)
    flower = list(chosen_flower.keys())[0]
    explain = list(chosen_flower.values())[0]


    # get first flower data from db (select emotion from flower_result where id = input)
    # get first flower data from db (select situation from flower_result where id = input)
    select_query = "SELECT COUNT(*) FROM flower_satisfaction WHERE id=%s"
    cur.execute(select_query, (input,))
    result =cur.fetchone()
    # flower_satisfaction database: insert id, chosen_flower
    #
    if result[0] == 0:
        cur.execute("INSERT INTO flower_satisfaction (id,chosen_flower) VALUES (%s,%s)", (input,flower))
    else:
        cur.execute("UPDATE flower_satisfaction SET chosen_flower = %s WHERE id = %s", (flower, input))
    cur.close()

    return render_template("final_page.html", flower = flower, explain = explain, input=input)


@app.route('/finalsecond/<input>')
def finalsecond(input):
    cur = config.conn.cursor()

    get_emotion_SQL = 'SELECT emotion FROM flower_result WHERE id = %s'
    get_situation_SQL = 'SELECT situation FROM flower_result WHERE id = %s'
    cur.execute(get_emotion_SQL, input)
    emotion = cur.fetchall()[0][0]
    print(f"emotion:{emotion}")
    cur.execute(get_situation_SQL, input)
    situation = cur.fetchall()[0][0]
    print(f"emotion:{situation}")

    chosen_flower = getflower.fromFlowerList(emotion,situation)

    flower = list(chosen_flower.keys())[1]
    explain = list(chosen_flower.values())[1]

    # flower_satisfaction database: insert id, chosen_flower, satisfaction
    #
    select_query = "SELECT COUNT(*) FROM flower_satisfaction WHERE id=%s"
    cur.execute(select_query, (input,))
    result =cur.fetchone()
    # flower_satisfaction database: insert id, chosen_flower
    #
    if result[0] == 0:
        cur.execute("INSERT INTO flower_satisfaction (id,chosen_flower) VALUES (%s,%s)", (input,flower))
    else:
        cur.execute("UPDATE flower_satisfaction SET chosen_flower = %s WHERE id = %s", (flower, input))
    cur.close()

    return render_template("final_page.html", flower = flower, explain = explain, input=input)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        input = request.form['input']
        print(input)
        return redirect(url_for('result', input=input))
    else:
        temp = None
    return redirect(url_for('predict',input=input))

@app.route('/val/<user_id>', methods=['POST','GET'])
def save(user_id):
    input = request.form['img_btn']
    if input == 'first':
        return redirect(url_for('finalfirst',input=user_id))
    elif input == 'second':
        return redirect(url_for('finalsecond',input=user_id))

@app.route('/goodfeedback/<input>', methods = ['POST'])
def goodfeedback(input):
    #update feedback to db
    cur = config.conn.cursor()
    update_SQL = 'UPDATE flower_satisfaction SET satisfaction = 1  WHERE id = %s'
    cur.execute(update_SQL, input)
    cur.close()

    return redirect(url_for('kkot'))

@app.route('/badfeedback/<input>', methods = ['POST'])
def badfeedback(input):
    #update feedback to db
    cur = config.conn.cursor()
    update_SQL = 'UPDATE flower_satisfaction SET satisfaction = 0  WHERE id = %s'
    cur.execute(update_SQL, input)
    cur.close()
    return redirect(url_for('kkot'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html") , 400

# 번들링된 scss 렌더링
assets.register('index_css', index_bundle)