from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
