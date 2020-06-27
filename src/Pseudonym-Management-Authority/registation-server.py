from flask import Flask, render_template, request, url_for
from tokenGenerator import TokenGenerator
from regDataManager import RegDataManager
from src.CommonVariables import Generals
import json

app = Flask(__name__)


@app.route('/register')
def register():
    return render_template('/index.html')


@app.route('/requestPseudonym', methods=['GET', 'POST'])
def requestPseudonym():
    if request.method == 'POST':
        data = request.form

    return data


@app.route('/success', methods=['GET', 'POST'])
def getPost():
    render_template('index.html')
    if request.method == 'POST':
        formData = request.form
        getRegData = TokenGenerator.generateToken(formData)
        regData = RegDataManager()
        regData.saveData(getRegData['formData'])
        regToken = getRegData['formData']['regToken']
        integrity = getRegData['integrity']
        return render_template("SuccessUser.html", token=regToken, integrity=integrity)


if __name__ == '__main__':
    app.config["CACHE_TYPE"] = "null"
    app.run(host='0.0.0.0')
