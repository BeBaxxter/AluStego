from SocialNetwork import TextPost, VideoPost, PhotoPost, Comment
import csv

class PostsReader():
    def readPosts(self):
        posts = []
        with open('testPosts.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                if row[0] == "text":
                    post = TextPost(row[0], row[1], row[2], row[3], row[4])
                    posts.append(post)
                if row[0] == "image":
                    post = PhotoPost(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    posts.append(post)
                if row[0] == "video":
                    post = VideoPost(row[0], row[1], row[2], row[3], row[4], row[5])
                    posts.append(post)
        return posts