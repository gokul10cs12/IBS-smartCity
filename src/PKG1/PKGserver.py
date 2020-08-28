import requests
from flask import Flask, request
from src.CommonVariables import Generals

app = Flask(__name__)


@app.route('/requestCertificate', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userToken = request.json
        requestToPma = requests.post(Generals.urlPseudonym, json=userToken)
        return requestToPma.json()


if __name__ == '__main__':
    app.config["CACHE_TYPE"] = "null"
    app.run(host='0.0.0.0', port=5300)
