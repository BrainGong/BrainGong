import flask;
from flask import render_template, request,url_for

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
    app.run()