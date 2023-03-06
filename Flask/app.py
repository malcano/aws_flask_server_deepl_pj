from flask import Flask, render_template, request, redirect, url_for, session
import config
import model, getFlower, create_id

md = model.model()
id = create_id.id()
print("create model instance!")
getflower = getFlower.getFlower()
print("create getflower instance!")

app = Flask(__name__)
app.secret_key = 'dsaklfjiodsjfioasdjfioajdsiofjaiosdj'

cur = config.conn.cursor()
# we can use cur like below codes
# cur.execute("쿼리문")
# cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
# conn.commit()

@app.route("/")
def kkot():
    user_id = id.newID()
    session['user_id'] = user_id
    return render_template("index.html")
@app.route('/result/<input>')
def result(input):#input: 사용자로부터 받는 메세지
    sentence = input
    sentiment = int(md.sentiment_predict(input))
    circumstance = int(md.circumstance_predict(input))
    user_id = session.get("user_id")

    rec_flower = getflower.fromFlowerList(sentiment, circumstance) # return value would be like [{"flower1":"sentence"},{"flower2":"sentence}]
    # 둘 중 마음에 드는 꽃을 선택해주세요

    sentence = "TEST MESSAGE: input message: " + str(input) +"\nsentiment predict: "+ getflower.getSentiment(sentiment) + \
               "circumstance predict: "+getflower.getCircumstance(circumstance) + '\n\n' + "둘 중 더 마음에 드는 꽃을 선택해주세요.\n\n"+\
                list(rec_flower[0].keys())[0]+": " + list(rec_flower[0].values())[0] + "\n"+ \
                list(rec_flower[1].keys())[0]+": " + list(rec_flower[1].values())[0] + " unique_id : " + str(user_id)

    # DB INSERT ID, SENTENCE, EMOTION, SITUATION


    return sentence
@app.route('/val')
def validation():
    user_id = session.get("user_id")

    # DB UPDATE CHOSEN FLOWER, SATISFACTION BY ID



    session.clear()


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        input = request.form['input']
        n_unique = id.newID()
        print(input)
        return redirect(url_for('result', input=input))
    else:
        temp = None
    return redirect(url_for('predict',input=input))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 400