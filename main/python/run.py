import os
from flask import Flask, render_template, request, Markup, redirect, url_for, flash
from werkzeug.utils import secure_filename
from SocialNetwork import TextPost, PhotoPost, VideoPost, PostsReader, Comment


UPLOAD_FOLDER = '../static/data/images/mdecken'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


#change the color theme here "color_day" or "color_night"
colorTheme = "color_day"
#colorTheme = "color_night"

currentUser = "Max Decken"
currentUserName ="mdecken"



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def start():
    return render_template("auth.html", colorTheme=colorTheme)

@app.route('/feed', methods = ['POST', 'GET'])
def feed():
    reader = PostsReader()
    posts = reader.readPosts()
    #posts.reverse()

    title = "Feed"
    return render_template("feed.html", title=title, posts=posts, colorTheme=colorTheme)

@app.route('/uploadText', methods = ['POST', 'GET'])
def uploadText():
    if request.method == 'POST':
        message = request.form["message"]
        reader = PostsReader()
        id = reader.lenPosts() + 1
        reader.addPost(TextPost(id, "text", currentUser, "../static/data/images/lcarmohn/img_avatar.png", "3h ago", message))
        return redirect("/feed")

@app.route('/uploadImage', methods = ['POST', 'GET'])
def uploadImage():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("/feed")


@app.route('/uploadVideo', methods=['POST', 'GET'])
def uploadVideo():
    return

@app.route('/addComment', methods=['POST', 'GET'])
def addComment():
    if request.method == 'POST':
        postID = request.form["postId"]
        message = request.form["message"]
        print(postID, message)
    else:
        postID = request.args.get('postId')
        message = request.args.get("message")
        return redirect(url_for('success', name=user))
    reader = PostsReader()
    id = reader.lenComments() + 1
    reader.addComment(Comment(id, postID, "../static/data/images/lcarmohn/img_avatar.png", currentUser, message))
    return redirect("/feed")

@app.route('/profile')
def profile():
    title = "Profile"
    return render_template("profile.html", title=title, colorTheme=colorTheme)

@app.route('/chats')
def chats():
    title = "Chats"
    return render_template('chats.html', title=title, colorTheme=colorTheme)

@app.route('/test')
def test():
    return posts[0].author