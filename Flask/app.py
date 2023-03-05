from flask import Flask, render_template, request, redirect, url_for
import config
import model


app = Flask(__name__)

cur = config.conn.cursor()
# we can use cur like below codes
# cur.execute("쿼리문")
# cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
# conn.commit()

@app.route("/")
def kkot():
    return render_template("index.html")
@app.route('/result')
def result():
    return 'hello'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('kkot',num=temp))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
