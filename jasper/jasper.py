# 1//0eGXWU1xfwMrzCgYIARAAGA4SNwF-L9Irqd2OtXbNOjwQ81H2fDAIK_NVEm-YueEPoPBAbpu2NMrhYEftNz8WxFboB1PA12_9SZw
# Example: firebase deploy --token "$FIREBASE_TOKEN"

from flask import Flask, render_template, request, redirect
import webbrowser
from jasper.push import pusher

app = Flask("home")

@app.route("/")
def home():
    extracted = pusher
    link_code_needToPrint = extracted.extract_link_code()
    info_extracted = extracted.extract_text()
    codeMax = extracted.extract_code_max()
    return render_template("home.html", 
                           link_code_needToPrint=link_code_needToPrint, 
                           codeMax=codeMax, 
                           info_extracted=info_extracted,
    )

@app.route("/register")
def register():
    
    return render_template("register.html")

@app.route("/code")
def code():
    return render_template("code.html")

url = "http://127.0.0.1:5000/"
webbrowser.open(url)
app.run('127.0.0.1', port=5000, debug=True)


