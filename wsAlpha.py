from flask import Flask, redirect, url_for, render_template, request
import addToNewsletterList, sys
import bcrypt

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/register")
def result():
    return render_template('register.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    output = request.form.to_dict()
    email = output["email"]
    addToNewsletterList.add_mailjet(email)
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
