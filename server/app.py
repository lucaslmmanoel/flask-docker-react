import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(msg="KALLIU GAY")

@app.route('/api/message')
def message():
    return jsonify(msg="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0")