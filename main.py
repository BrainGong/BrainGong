import flask;
import os
from flask import render_template, request,url_for

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')