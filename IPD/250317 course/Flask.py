from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>hello world</h1>"
@app.route("/ok")
def ok():
    return "<h1>ok</h1>"
@app.route("/yes")
def yes():
    return "<h1>yes</h1>"
app.run()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)