from flask import Flask, render_template, request, redirect, url_for, session
from flask_assets import Environment, Bundle
import config
import model, getFlower, create_id

md = model.model()
print("create model instance!")
getflower = getFlower.getFlower()
print("create getflower instance!")

app = Flask(__name__)

assets = Environment(app)
scss = Bundle('app.scss', filters='pyscss', output='css/app.css')
assets.register('scss_all', scss)
app.secret_key = 'dsaklfjiodsjfioasdjfioajdsiofjaiosdj'
# we can use cur like below codes
# cur.execute("쿼리문")
# cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
# conn.commit()

@app.route("/")
def kkot():
    return render_template("index.html")
@app.route('/result/<input>')
def result(input):#input: 사용자로부터 받는 메세지
    id = create_id.id()
    cur = config.conn.cursor()

    #need to insert to Database
    sentence = input
    sentiment = int(md.sentiment_predict(input))
    circumstance = int(md.circumstance_predict(input))
    rec_flower = getflower.fromFlowerList(sentiment, circumstance) # return value would be like {"flower1":"sentence","flower2":"sentence}
    user_id = id.newID()
    del id
    #need to parse to select_page.html


    first_flower = list(rec_flower.keys())[0]
    second_flower = list(rec_flower.values())[0]
    first_flower_explain = list(rec_flower.keys())[1]
    second_flower_explain = list(rec_flower.values())[1]

    #
    # first_flower = list(rec_flower[0].keys())[0]
    # second_flower = list(rec_flower[0].values())[0]
    # first_flower_explain = list(rec_flower[1].keys())[0]
    # second_flower_explain = list(rec_flower[1].values())[0]

    # 둘 중 마음에 드는 꽃을 선택해주세요
    #
    # sentence = "TEST MESSAGE: input message: " + str(input) +"\nsentiment predict: "+ getflower.getSentiment(sentiment) + \
    #            "circumstance predict: "+getflower.getCircumstance(circumstance) + '\n\n' + "둘 중 더 마음에 드는 꽃을 선택해주세요.\n\n"+\
    #             list(rec_flower[0].keys())[0]+": " + list(rec_flower[0].values())[0] + "\n"+ \
    #             list(rec_flower[1].keys())[0]+": " + list(rec_flower[1].values())[0] + " unique_id : " + str(user_id)

    # DB INSERT ID, SENTENCE, EMOTION, SITUATION
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
    explain = list(chosen_flower.keys())[1]


    # get first flower data from db (select emotion from flower_result where id = input)
    # get first flower data from db (select situation from flower_result where id = input)


    # flower_satisfaction database: insert id, chosen_flower, satisfaction
    #
    cur.close()

    return render_template("final_page.html", flower = flower, explain = explain)


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

    flower = list(chosen_flower.values())[0]
    explain = list(chosen_flower.values())[1]

    # flower_satisfaction database: insert id, chosen_flower, satisfaction
    #
    cur.close()

    return render_template("final_page.html", flower = flower, explain = explain)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html") , 400