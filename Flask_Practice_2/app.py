from flask import Flask, request,redirect,url_for,session,Response,render_template

app=Flask(__name__)
app.secret_key="1234567890"

@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_submit():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="123":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("In_valid Credentials. Try Again",mimetype="text/plane")
@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("welcome.html")
    else:
        return redirect(url_for("login_page"))
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login_page"))
if __name__=="__main__":
    app.run(debug=True)