# 1//0eGXWU1xfwMrzCgYIARAAGA4SNwF-L9Irqd2OtXbNOjwQ81H2fDAIK_NVEm-YueEPoPBAbpu2NMrhYEftNz8WxFboB1PA12_9SZw
# Example: firebase deploy --token "$FIREBASE_TOKEN"
# github-action-744496441

from flask import Flask, render_template, request, redirect
import webbrowser
from push import pusher

app = Flask("home")

@app.route("/")
def home():
    extracted = pusher
    info_extracted = extracted.extract_link_code()
    codeMax = extracted.extract_code_max()
    texts = extracted.extract_text()
    return render_template("index.html", 
                           info_extracted=info_extracted, 
                           codeMax=codeMax,
                           texts=texts, 
    )

@app.route("/register")
def register():
    
    return render_template("register.html")

@app.route("/code")
def code():

    return render_template("code.html")

# url = "http://127.0.0.1:5000/"
app.run('127.0.0.1', port=5000, debug=True)
# webbrowser.open(url)


