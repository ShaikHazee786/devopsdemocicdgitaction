from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():

    return "<h1 style='color:blue'>Hello, This is CICD with GitAction for Flask App</h1>"
@app.route("/about")
def about():
    return "Welcomt to my about page"

@app.route("/service")
def service():
    return "Welcome to service page"

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
