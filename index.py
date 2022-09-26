from flask import Flask , render_template, request
import qrcode 
import os 



app = Flask(__name__)

import datetime

date = datetime.datetime.now()

@app.route("/")
def home():
    return render_template("index.html", date=date.year)

@app.route("/", methods =["GET", "POST"])
def qr():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        link = request.form.get("qr")
        print(link)
        #making the qr code
        img = qrcode.make(link)
        #saving the qr code as PNG extension
        img.save("./static/qr.png", "PNG")


    return render_template("qr.html", date=date.year)


