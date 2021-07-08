from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World - maybe football is coming home"

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
