from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the first page"

## return something from the route
## learn how to manage errors


if __name__ == "__main__":
    app.run(debug = True)