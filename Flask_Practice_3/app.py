from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")
@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    if username=="abdullah" and password=="1234":
        return render_template("welcome.html")
    else:
        return render_template("invalid_user.html")
if __name__=="__main__":
    app.run(debug=True)