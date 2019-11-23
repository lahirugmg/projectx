#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/getinfo')
def index():
    return jsonify({"studentName":"John","studentId":"23432"}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

