from Post import TextPost, VideoPost, PhotoPost, Comment
import csv
from datetime import datetime

class PostsReader():
    def readPosts(self):
        comments = self.readComments()
        posts = []
        with open('alustego/alustego/testPosts.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                if row[1] == "text":
                    time = self.getTime(int(row[4]))
                    post = TextPost(row[0], row[1], row[2], row[3], time, row[5])
                    for comment in comments:
                        if comment.postID == post.id:
                            post.addComment(comment)
                    posts.append(post)
                if row[1] == "image":
                    time = self.getTime(int(row[4]))
                    post = PhotoPost(row[0], row[1], row[2], row[3], time, row[5], row[6], row[7])
                    for comment in comments:
                        if comment.postID == post.id:
                            post.addComment(comment)
                    posts.append(post)
                if row[1] == "video":
                    time = self.getTime(int(row[4]))
                    post = VideoPost(row[0], row[1], row[2], row[3], time, row[5], row[6])
                    for comment in comments:
                        if comment.postID == post.id:
                            post.addComment(comment)
                    posts.append(post)
        return posts

    def addPost(self, post):
        with open('alustego/alustego/testPosts.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if post.type == "text":
                writer.writerow([post.id, post.type, post.author, post.avatar, post.time, post.text])

            if post.type == "image":
                writer.writerow([post.id, post.type, post.author, post.avatar, post.time, post.photo, post.alt, post.title])

            if post.type == "video":
                writer.writerow([post.id, post.type, post.author, post.avatar, post.time, post.video, post.poster])

    def lenPosts(self):
        with open('alustego/alustego/testPosts.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            i = 0
            for row in reader:
                i = i + 1

        return i

    def readComments(self):
        comments = []
        with open('alustego/alustego/testComments.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                comment = Comment(row[0], row[1], row[2], row[3], row[4])
                comments.append(comment)

        return comments

    def addComment(self, comment):
        with open('alustego/alustego/testComments.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([comment.id, comment.postID, comment.avatar, comment.name, comment.text])

    def lenComments(self):
        comments = []
        with open('alustego/alustego/testComments.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            i = 0
            for row in reader:
                i = i + 1

        return i

    def getTime(self, timestamp):
        now = datetime.now().timestamp()
        time = int(now) - timestamp
        if time < 60:
            return str(int(time)) + "sec ago"
        elif time > 59 and time < 3600:
            return str(int(time/60)) + "min ago"
        elif time > 3599 and time < 86400:
            return str(int(time/3600)) + "h ago"
        elif time > 86399:
            return str(int(time/86400)) + "d ago"
