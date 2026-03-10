from flask import Flask, request

app= Flask(__name__)
@app.route("/")
def home():
    return "Hello This is my First Flask App"
@app.route("/about")
def about():
    return "This is about page"
@app.route("/content")
def content():
    return "This is content page"
@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        return "You are sending Data"
    else:
        return "You are Viewing Data"
if __name__ == "__main__":
    app.run(debug=True)