import os
from flask import Flask, render_template, request, Markup, redirect
from werkzeug.utils import secure_filename

# for server deploy change to:  from main.common
from main.common.posts.Post import TextPost, PhotoPost, VideoPost, Comment
from main.common.posts.postHandler import PostsReader
from main.common.user.User import User
from datetime import datetime

app = Flask(__name__)

# change the color theme here "color_day" or "color_night"
colorTheme = "color_day"
# colorTheme = "color_night"

currentUser = User(1, "Max Decken", "mdecken", "1234", "../static/data/images/lcarmohn/img_avatar.png")

app.config["IMAGE_UPLOADS"] = "static/data/uploads/"
app.config["VIDEO_UPLOADS"] = "static/data/uploads/"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["ALLOWED_VIDEO_EXTENSIONS"] = ["MP4", "MOV"]


def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_video(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_VIDEO_EXTENSIONS"]:
        return True
    else:
        return False


def renameFile(filename):
    ext = filename.rsplit(".", 1)[1]
    name = filename.rsplit(".", 1)[0]
    newName = currentUser.userName + datetime.today().strftime('%Y-%m-%d') + "_" + name.lower()
    return newName + "." + ext


@app.route('/')
def start():
    title = "Welcome!"
    site = "start"
    return render_template("auth.html", title=title, site=site, colorTheme=colorTheme)


@app.route('/feed', methods=['POST', 'GET'])
def feed():
    reader = PostsReader()
    posts = reader.readPosts()

    title = "Feed"
    site = "feed"
    return render_template("feed.html", title=title, site=site, posts=posts, colorTheme=colorTheme)


@app.route('/uploadText', methods=['POST', 'GET'])
def uploadText():
    if request.method == 'POST':
        message = request.form["message"]
        reader = PostsReader()
        id = reader.lenPosts() + 1
        time = int(datetime.now().timestamp())
        reader.addPost(TextPost(id, "text", currentUser.name, currentUser.avatar, time, message))
        return redirect("/feed")


@app.route('/uploadImage', methods=['POST', 'GET'])
def uploadImage():
    if request.method == 'POST':
        if request.files:
            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect("/feed")
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                # rename file here
                filename = renameFile(filename)
                path = os.path.join(app.config["IMAGE_UPLOADS"], filename)
                image.save(os.path.join(os.path.dirname(__file__), path))
                print(path)
                reader = PostsReader()
                id = reader.lenPosts() + 1
                alt = str(image.filename)
                title = "Posted by " + currentUser
                time = int(datetime.now().timestamp())
                reader.addPost(
                    PhotoPost(id, "image", currentUser.name, currentUser.avatar, time, "../" + path, alt, title))
                return redirect("/feed")
            else:
                print("That file extension is not allowed")
                return redirect(request.url)


@app.route('/uploadVideo', methods=['POST', 'GET'])
def uploadVideo():
    if request.method == 'POST':
        if request.files:
            video = request.files["video"]

            if video.filename == "":
                print("No filename")
                return redirect("/feed")
            if allowed_video(video.filename):
                filename = secure_filename(video.filename)
                # rename file here
                filename = renameFile(filename)
                path = os.path.join(app.config["VIDEO_UPLOADS"], filename)
                video.save(os.path.join(os.path.dirname(__file__), path))
                reader = PostsReader()
                id = reader.lenPosts() + 1
                time = int(datetime.now().timestamp())
                reader.addPost(
                    VideoPost(id, "video", currentUser.name, currentUser.avatar, time, "../" + path, "posterimage.jpg"))
                return redirect("/feed")
            else:
                print("That file extension is not allowed")
                return redirect(request.url)


@app.route('/addComment', methods=['POST', 'GET'])
def addComment():
    if request.method == 'POST':
        postID = request.form["postId"]
        message = request.form["message"]
    reader = PostsReader()
    id = reader.lenComments() + 1
    reader.addComment(Comment(id, postID, currentUser.avatar, currentUser.userName, message))
    url = "/feed#post_" + str(postID)
    return redirect(url)


@app.route('/profile')
def profile():
    title = "Profile"
    site = "profile"
    reader = PostsReader()
    allPosts = reader.readPosts()
    posts = []
    for post in allPosts:
        if post.author == currentUser.name:
            posts.append(post)
    return render_template("profile.html", site=site, title=title, colorTheme=colorTheme, posts=posts)


@app.route('/chats')
def chats():
    title = "Chats"
    site = "chats"
    return render_template('chats.html', site=site, title=title, colorTheme=colorTheme)


if __name__ == "__main__":
    app.run()
