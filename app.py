from flask import Flask, jsonify, request
import PAYE
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', static_url_path='', static_folder='static')
def hello_world():
    return 'Hello World!'

@app.route('/getNetIncome/', methods=['POST'])
def netIncome():
    cross_income = request.get_json()
    cross = float(cross_income["gross_income"])
    return jsonify(cross - PAYE.totalTax(cross))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
