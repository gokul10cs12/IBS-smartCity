from flask import Flask, render_template, request, url_for
from tokenGenerator import TokenGenerator


app = Flask(__name__)


@app.route('/register')
def register():
    return render_template('/index.html')


@app.route('/success', methods=['GET', 'POST'])
def getPost():
    render_template('index.html')
    if request.method == 'POST':
        getRegData = TokenGenerator.generateToken(request.form)
        print(getRegData)
        return request.form


if __name__ == '__main__':
    app.config["CACHE_TYPE"] = "null"
    app.run(host='0.0.0.0')
