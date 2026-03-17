from flask import Flask, render_template, redirect, url_for, flash, request

app=Flask(__name__)
app.secret_key = "mysecretkey123"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/feedback",methods=["POST","GET"])
def feedback():
    if request.method=="POST":
        name=request.form.get("name")
        message=request.form.get("message")
        if not name:
            flash("Name cant not be empty")
            return redirect(url_for("feedback"))
        flash(f"Thanks {name} your form was Saved")
        return redirect(url_for("thankyou", name=name))
    return render_template("feedback.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__=="__main__":
    app.run(debug=True)
