from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Welcome to my home page, goto results page with your score"


@app.route('/results/<int:marks>')
def calculate(marks):
    result = ""
    if marks < 50:
        result = "failed"
    else:
        result = "succ"
    return (redirect(url_for(result, score=marks)))


@app.route('/Fail/<int:score>')
def failed(score):
    return "You got less marks hence you failed, marks : " + str(score)


@app.route('/Success/<int:score>')
def succ(score):
    return "You got good marks hence you passed, marks : " + str(score)


if __name__ == "__main__":
    app.run(debug=True)
