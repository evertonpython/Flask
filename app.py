from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"

@app.route("/ola")
def ola():
    return "Ola!!!"

@app.route("/user/<string:user>")
def user(user):
    return "Ola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)



if __name__ == '__main__':
    app.run(debug=True)
