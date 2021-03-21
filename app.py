from flask import Flask, jsonify, request
import PAYE
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getNetIncome/', methods=['POST'])
def netIncome():
    cross_income = request.get_json()
    return cross_income
    #return jsonify(PAYE.totalTax())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
