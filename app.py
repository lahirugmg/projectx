#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/getstudents')
def index():
    return jsonify({"students":[{"studentName":"John Botha","studentId":"23432"},{"studentName":"Nickalas Cage","studentId":"90098"},{"studentName":"Kasun Pathirana","studentId":"334321"}]}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

