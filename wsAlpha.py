from flask import Flask, redirect, url_for, render_template, request, flash
import addToNewsletterList, sys
import bcrypt

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/registered", methods=["POST", "GET"])
def registered():
    output = request.form.to_dict()
    email = output["email"]
    addToNewsletterList.add_mailjet(email)
    flash('You have registered successfully', 'info')
    return render_template("index.html")

@app.route("/dashboard")
def profile():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
