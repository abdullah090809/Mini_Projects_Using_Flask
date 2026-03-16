from flask import Flask, render_template

app=Flask(__name__)

books = ["Python Crash Course", "Clean Code", "The Pragmatic Programmer"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/books")
def booklist():
    return render_template("books.html",books=books)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__==("__main__"):
    app.run(debug=True)