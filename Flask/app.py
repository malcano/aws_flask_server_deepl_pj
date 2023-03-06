from flask import Flask, render_template, request, redirect, url_for
import config
import model, getFlower

md = model.model()
getflower = getFlower.getFlower()

app = Flask(__name__)

cur = config.conn.cursor()
# we can use cur like below codes
# cur.execute("쿼리문")
# cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
# conn.commit()

@app.route("/")
def kkot():
    return render_template("index.html")
@app.route('/result/<input>')
def result(input):
    sentiment = int(md.sentiment_predict(input))
    circumstance = int(md.circumstance_predict(input))
    rec_flower = getflower.fromFlowerList(sentiment, circumstance) # return value would be like [{"flower1":"sentence"},{"flower2":"sentence}]
    sentence = "input message: " + str(input) +"\nsentiment predict: "+ getflower.getSentiment(sentiment) + \
               "circumstance predict: "+getflower.getCircumstance(circumstance) + '\n\n' + "당신에게 두 꽃을 추천드립니다.\n\n"+\
                list(rec_flower[0].keys())[0]+": " + list(rec_flower[0].values())[0] + "\n"+ \
                list(rec_flower[1].keys())[0]+": " + list(rec_flower[1].values())[0]
    return sentence
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        input = request.form['input']
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