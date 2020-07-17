import json

from flask import Flask, render_template, request, url_for, jsonify
from tokenGenerator import TokenGenerator
from regDataManager import RegDataManager
from pseudonymGenerator import PseudonymGenerator

from src.CommonVariables import Generals

app = Flask(__name__)

regData = RegDataManager()


@app.route('/register')
def register():
    return render_template('/index.html')


@app.route('/requestPseudonym', methods=['GET', 'POST'])
def requestPseudonym():
    response = {}
    if request.method == 'POST':
        token = request.json
        existCheck = regData.verifyToken(token['regToken'])
        if existCheck:
            response['pseudonym'] = PseudonymGenerator.generatePseudonym()
            response['status'] = 'success'
            response['regToken'] = token['regToken']
            return jsonify(response), 200
        else:
            response['status'] = "Authentication Failed"
            return jsonify(response), 200


@app.route('/success', methods=['GET', 'POST'])
def registerUser():
    if request.method == 'POST':
        formData = request.form
        getRegData = TokenGenerator.generateToken(formData)
        status = regData.saveData(getRegData['formData'])
        if status == Generals.DB_ERROR:
            return render_template("FailRegUser.html", message=Generals.DB_ERROR)
        else:
            regToken = getRegData['formData']['regToken']
            integrity = getRegData['integrity']
            return render_template("SuccessUser.html", token=regToken, integrity=integrity)


if __name__ == '__main__':
    app.config["CACHE_TYPE"] = "null"
    app.run(host='0.0.0.0')
