# for server deploy change to:  from main.common
# also change csv import   to:  var/www/alustego/main/database/
from .Post import TextPost, VideoPost, PhotoPost, Comment
import csv
from datetime import datetime
from common.database import PostsTableFunctions, UsersTableFunctions, CommentsTableFunctions

class PostsReader():

    def readFeedPosts(self, user_name):
        postIDs = PostsTableFunctions.get_news_feed_post_ids(user_name)
        return self.readPosts(postIDs)


    def readUserPosts(self, user_name):
        postIDs = PostsTableFunctions.get_all_posts_of_user(user_name)
        return self.readPosts(postIDs)


    def readPosts(self, postIDs):
        #comments = self.readComments()
        posts = []
        #with open('../main/dummy_database/testPosts.csv', "r", newline='') as csvfile:
         #   reader = csv.reader(csvfile, delimiter=';', quotechar='"')
          #  for row in reader:
           #     if row[1] == "text":
            #        time = self.getTime(int(row[4]))
              #      post = TextPost(row[0], row[1], row[2], row[3], time, row[5])
             #       for comment in comments:
               #         if comment.postID == post.id:
                #            post.addComment(comment)
                 #   posts.append(post)
                #if row[1] == "image":
                 #   time = self.getTime(int(row[4]))
                  #  post = PhotoPost(row[0], row[1], row[2], row[3], time, row[5], row[6], row[7])
                   # for comment in comments:
                    #    if comment.postID == post.id:
                     #       post.addComment(comment)
                    #posts.append(post)
                #if row[1] == "video":
                 #   time = self.getTime(int(row[4]))
                  #  post = VideoPost(row[0], row[1], row[2], row[3], time, row[5], row[6])
                   # for comment in comments:
                    #    if comment.postID == post.id:
                     #       post.addComment(comment)
                   # posts.append(post)

        for postID in postIDs:
            if PostsTableFunctions.get_type_of_post(postID) == 1: #text
                type = PostsTableFunctions.get_type_of_post(postID)
                author = UsersTableFunctions.get_username(PostsTableFunctions.get_post_author_id(postID))
                avatar = UsersTableFunctions.get_user_profile_pic(author)
                time = PostsTableFunctions.get_post_date_time(postID)
                text = PostsTableFunctions.get_post_content(postID)
                comments = CommentsTableFunctions.get_all_comments_of_post(postID)
                post = TextPost(postID, type, author, avatar, time, text)
                #for comment in comments:
                    #com_name = CommentsTableFunctions.get_username(comment)
                    #com_avatar = UsersTableFunctions.get_user_profile_pic(com_name)
                    #com_text = CommentsTableFunctions.get
                    #post.addComment(Comment())
                    #missing code here
                posts.append(post)

                if PostsTableFunctions.get_type_of_post(postID) == 2:  #image
                    type = PostsTableFunctions.get_type_of_post(postID)
                    author = UsersTableFunctions.get_username(PostsTableFunctions.get_post_author_id(postID))
                    avatar = UsersTableFunctions.get_user_profile_pic(author)
                    time = PostsTableFunctions.get_post_date_time(postID)
                    photo = PostsTableFunctions.get_post_content(postID)
                    comments = CommentsTableFunctions.get_all_comments_of_post(postID)
                    alt = "A picture " + author
                    title = alt
                    post = PhotoPost(postID, type, author, avatar, time, photo, alt, title)
                    #for comment in comments:
                        #com_name = CommentsTableFunctions.get_username(comment)
                        #com_avatar = UsersTableFunctions.get_user_profile_pic(com_name)
                        #com_text = CommentsTableFunctions.get
                        #post.addComment(Comment())
                        # missing code here
                    posts.append(post)

                if PostsTableFunctions.get_type_of_post(postID) == 3:  #video
                    type = PostsTableFunctions.get_type_of_post(postID)
                    author = UsersTableFunctions.get_username(PostsTableFunctions.get_post_author_id(postID))
                    avatar = UsersTableFunctions.get_user_profile_pic(author)
                    time = PostsTableFunctions.get_post_date_time(postID)
                    video = PostsTableFunctions.get_post_content(postID)
                    comments = CommentsTableFunctions.get_all_comments_of_post(postID)
                    poster = "posterimage.jpg"
                    post = VideoPost(postID, type, author, avatar, time, video, poster)
                    #for comment in comments:
                        #com_name = CommentsTableFunctions.get_username(comment)
                        #com_avatar = UsersTableFunctions.get_user_profile_pic(com_name)
                        #com_text = CommentsTableFunctions.get
                        #post.addComment(Comment())
                        # missing code here
                    posts.append(post)

        return posts



    def addPost(self, post):
       # with open('../main/dummy_database/testPosts.csv', 'a', newline='') as csvfile:
       #     writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       #     if post.type == "text":
       #         writer.writerow([post.id, post.type, post.author, post.avatar, post.time, post.text])
#
 #           if post.type == "image":
  #              writer.writerow(
   #                 [post.id, post.type, post.author, post.avatar, post.time, post.photo, post.alt, post.title])
#
 #           if post.type == "video":
  #              writer.writerow([post.id, post.type, post.author, post.avatar, post.time, post.video, post.poster])
        if post.type == "text":
            PostsTableFunctions.insert_new_post((post.author, post.author, post.text, 1))
        if post.type == "image":
            PostsTableFunctions.insert_new_post((post.author, post.author, post.text, 1))
        if post.type == "video":
            PostsTableFunctions.insert_new_post((post.author, post.author, post.text, 1))

    def lenPosts(self): #not needed in the future
        with open('../main/dummy_database/testPosts.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            i = 0
            for row in reader:
                i = i + 1

        return i

    def readComments(self): #not needed in the future
        comments = []
        with open('../main/dummy_database/testComments.csv', "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                comment = Comment(row[0], row[1], row[2], row[3], row[4])
                comments.append(comment)

        return comments

    def addComment(self, comment):
        #with open('../main/dummy_database/testComments.csv', 'a', newline='') as csvfile:
        #    writer = csv.writer(csvfile, delimiter=';',
        #                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #    writer.writerow([comment.id, comment.postID, comment.avatar, comment.name, comment.text])
        CommentsTableFunctions.insert_new_comment((comment.postID, comment.name, comment.text))

    def lenComments(self): #not needed in the future
        comments = []
        with open('../main/dummy_database/testComments.csv', "r", newline='') as csvfile:
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
            return str(int(time / 60)) + "min ago"
        elif time > 3599 and time < 86400:
            return str(int(time / 3600)) + "h ago"
        elif time > 86399:
            return str(int(time / 86400)) + "d ago"
