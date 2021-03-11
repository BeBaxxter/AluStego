from flask import Flask, render_template, request, Markup

app = Flask(__name__)



@app.route('/')
def start():
    return render_template("login.html")

@app.route('/feed')
def feed():
    title = "Feed"
    return render_template("feed.html", title=title)

@app.route('/profile')
def profile():
    title = "Profile"
    return render_template("profile.html", title=title)

@app.route('/chats')
def chats():
    title = "Chats"
    return render_template('chats.html', title=title)