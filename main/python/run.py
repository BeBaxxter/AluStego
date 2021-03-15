from flask import Flask, render_template, request, Markup
from SocialNetwork import PostsReader, Comment

app = Flask(__name__)

#Setup blow just for testing!!! (placeholder post and comments)
reader = PostsReader()
posts = reader.readPosts()
posts[0].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))
posts[0].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))
posts[0].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))

posts[1].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))
posts[1].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))
posts[1].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))

posts[2].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))
posts[2].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))
posts[2].addComment(Comment("../static/data/images/lcarmohn/img_avatar.png", "name", "Das ist ein Kommmentar indem ich irgendwas tolles über deinen Beitrag schreibe. Eigentlich ist das ein Dummytext um vernünftige CSS Style zu testen. Warum liest du das eigentlich noch? Hast du nichts zu tun?"))
#end test setup


#change the color theme here "color_day" or "color_night"
colorTheme = "color_day"
#colorTheme = "color_night"


@app.route('/')
def start():
    return render_template("login.html", colorTheme=colorTheme)

@app.route('/feed')
def feed():
    title = "Feed"
    return render_template("feed.html", title=title, posts=posts, colorTheme=colorTheme)

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