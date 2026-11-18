#web app
from flask import Flask,render_template,request
import joblib
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    q = request.form.get("q")
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = float(request.form.get("q"))
    model = joblib.load('dbs.jl')
    pred = model.predict([[q]])
    r = pred[0][0]
    return(render_template("main.html", r=r))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    q = float(request.form.get("q"))
    return(render_template("dbs.html"))

if __name__ == "__main__":
    app.run()