from flask import Flask, redirect, url_for, render_template, request, flash
import addToNewsletterList, removeFromNewsletter, sys
import bcrypt

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    addToNewsletterList.add_mailjet(email)
    return redirect("/")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        return redirect("/dashboard")
    else:
        return render_template("login.html")

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/dashboard", methods=["POST"])
def profile():
    email_login = request.form.get("email_login")
    username = ""
    for i in email_login:
        if i=="@":
            break
        else:
            username += i
    return render_template('dashboard.html', email=username)

@app.route("/unsubscribe", methods=["POST"])
def unsubscribe():
    email = request.form.get("email")
    removeFromNewsletter.remove_mailjet(email)
    flash('You have unsubcribed successfully', 'info')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
