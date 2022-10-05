from flask import Flask


credentials = [
    {
        "username":"goni",
        "password":"oct5"
    },
    {
        "username":"test",
        "password":"oct6"
    }
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"