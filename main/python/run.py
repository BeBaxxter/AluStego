import os
from flask import Flask, render_template, request, Markup, redirect
from SocialNetwork import TextPost, PhotoPost, VideoPost, PostsReader, Comment


app = Flask(__name__)

#change the color theme here "color_day" or "color_night"
colorTheme = "color_day"
#colorTheme = "color_night"

currentUser = "Max Decken"
currentUserName ="mdecken"

app.config["IMAGE_UPLOADS"] = os.path.join(os.path.dirname(__file__) ,"static/data/uploads/")
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


@app.route('/')
def start():
    return render_template("auth.html", colorTheme=colorTheme)

@app.route('/feed', methods = ['POST', 'GET'])
def feed():
    reader = PostsReader()
    posts = reader.readPosts()

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
        if request.files:
            image = request.files["image"]
            print(image)
            path = image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            reader = PostsReader()
            id = reader.lenPosts() + 1
            alt = str(image.filename)
            title = "Posted by " + currentUser
            reader.addPost(PhotoPost(id, "image", currentUser, "../static/data/images/lcarmohn/img_avatar.png", "3h ago", path, alt, title))
            return redirect("/feed")



@app.route('/uploadVideo', methods=['POST', 'GET'])
def uploadVideo():
    return

@app.route('/addComment', methods=['POST', 'GET'])
def addComment():
    if request.method == 'POST':
        postID = request.form["postId"]
        message = request.form["message"]
    reader = PostsReader()
    id = reader.lenComments() + 1
    reader.addComment(Comment(id, postID, "../static/data/images/lcarmohn/img_avatar.png", currentUserName, message))
    return redirect("/feed")

@app.route('/profile')
def profile():
    title = "Profile"
    reader = PostsReader()
    allPosts = reader.readPosts()
    posts = []
    for post in allPosts:
        if post.author == currentUser:
            posts.append(post)
    return render_template("profile.html", title=title, colorTheme=colorTheme, posts=posts)

@app.route('/chats')
def chats():
    title = "Chats"
    return render_template('chats.html', title=title, colorTheme=colorTheme)

if __name__ == "__main__":
  app.run()