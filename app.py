from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello,This is Srihitha"

@app.route("/about")
def about():
    return "Welcome to my about page"

@app.route("/service")
def service():
    return "Welcome to service page1"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
