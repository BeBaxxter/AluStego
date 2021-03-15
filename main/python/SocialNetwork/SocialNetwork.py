from SocialNetwork import TextPost, VideoPost, PhotoPost, Comment
import csv

class PostsReader():
    def readPosts(self):
        comments = self.readComments()
        posts = []
        with open('testPosts.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                if row[1] == "text":
                    post = TextPost(row[0], row[1], row[2], row[3], row[4], row[5])
                    for comment in comments:
                        if comment.postID == post.id:
                            post.addComment(comment)
                    posts.append(post)
                if row[1] == "image":
                    post = PhotoPost(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    for comment in comments:
                        if comment.postID == post.id:
                            post.addComment(comment)
                    posts.append(post)
                if row[1] == "video":
                    post = VideoPost(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    for comment in comments:
                        if comment.postID == post.id:
                            post.addComment(comment)
                    posts.append(post)
        return posts

    def addPost(self, post):
        with open('testPosts.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([post.type, post.author, post.avatar, post.time, post.text])

    def readComments(self):
        comments = []
        with open('testComments.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                comment = Comment(row[0], row[1], row[2], row[3], row[4])
                comments.append(comment)

        return comments

    def addComment(self, comment):
        with open('testComments.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([comment.id, comment.postID, comment.avatar, comment.name, comment.text])

    def lenComments(self):
        comments = []
        with open('testComments.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            i = 0
            for row in reader:
                i = i + 1

        return i