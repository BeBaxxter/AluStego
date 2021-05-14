import sqlite3
from sqlite3 import Error
#from . import *
from datetime import datetime

#from common.database import PostsTableFunctions
from common.database import FriendsTableFunctions
from common.database import LikesTableFunctions
from common.database import  UsersTableFunctions
from common.database import CommentsTableFunctions
from common.database import  TableCreationFunctions

# Insert Functions:

def insert_new_post(values):
    """ inserts a new post into the database
    :param values: 1.: author name, 2.: og author name (post might be a repost,
                   then name of the original author, otherwise same as author name),
                   3.: content of the post, type_of_post (1 = Text, 2 = Pic, 3 = Vid)
    return: None
    """
    try:
        time = int(datetime.now().timestamp())
        author_id = UsersTableFunctions.get_user_id(values[0])
        og_author_id = UsersTableFunctions.get_user_id(values[1])
        conn = TableCreationFunctions.create_connection()
        c = conn.cursor()
        c.execute("""
            INSERT INTO posts (author_id, og_author_id, date_time, content, type_of_post, number_of_likes) 
            VALUES (?, ?, ?, ?, ?, 0);""", (author_id, og_author_id, time, values[2], values[3], ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


# Delete Functions:

def delete_post(post_id):
    """ deletes a given post including likes and comments
    :param post_id: post_id
    :return: None
    """
    try:
        CommentsTableFunctions.delete_all_comments_of_post(post_id)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM likes WHERE like_post_id = ?;", (post_id, ))
        cur.execute(f"DELETE FROM posts WHERE post_id=?;", (post_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def delete_all_posts_of_user(user_id):
    """ deletes all posts of a given user including likes and comments
    :param user_id: ID of the user who's posts shall be deleted
    :return: None
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        post_id_tuple = get_all_posts_of_user(user_id)
        if post_id_tuple is not None:
            for post in post_id_tuple:
                cur.execute(f"DELETE FROM likes WHERE like_post_id = ?;", (post, ))

        cur.execute(f"DELETE FROM posts WHERE author_id = ? OR og_author_id = ?;", (user_id, user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# seemingly not needed
# def delete_all_likes_on_posts_of_user(user_id):
#     """ deletes all likes on posts of a given user
#     :param user_id:
#     :return: None
#     """
#     try:
#         conn = create_connection()
#         cur = conn.cursor()
#         post_id_tuple = get_all_posts_of_user(user_id)
#         if post_id_tuple is not None:
#             for post in post_id_tuple:
#                 cur.execute(f"DELETE FROM likes WHERE like_post_id = ?;", (post, ))
#         conn.commit()
#         conn.close()
#     except Error as e:
#         print(e)
#         conn.rollback()


# Select Functions:

def get_news_feed_post_ids(user_name):
    """ returns the post_ids of the posts of all friends of a given user to display on the home feed
        :param user_name
        :return: post_id's in a Tuple
        """
    try:
        friends_of_user = FriendsTableFunctions.get_all_friends_ids(user_name)
        list_of_post_ids = []
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        if friends_of_user is not None:
            for friend in friends_of_user:
                cur.execute(f"""
                                    SELECT post_id FROM posts
                                    WHERE author_id = ?;""", (friend,))
                row = cur.fetchall()
                if row:
                    list_of_post_ids.append(row)
            conn.commit()
            conn.close()
            if row:
                tuple_of_post_ids = ()
                for post in list_of_post_ids[0]:
                    tuple_of_post_ids = tuple_of_post_ids + post
                if tuple_of_post_ids:
                    return tuple_of_post_ids
                else:
                    return None
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_all_posts_of_user(user_name):
    """ returns posts of a given user
        :param user_name
        :return: Tuple with all post_id's of that user
        """
    try:
        user_id = UsersTableFunctions.get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                            SELECT post_id FROM posts
                            WHERE author_id = ? OR og_author_id = ?;""", (user_id, user_id, ))
        row = cur.fetchall()
        conn.commit()
        conn.close()
        if row:
            posts_tuple = ()
            for post in row:
                posts_tuple = posts_tuple + post
            print(posts_tuple)
            return posts_tuple
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_post_number_of_likes(post_id):
    """ returns the number of likes a given post has
    :param post_id: post_id
    :return: number_of_likes (Integer)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT number_of_likes FROM posts
                        WHERE post_id = ?;""", (post_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_post_id(values):
    """ returns post_id of a given post
    :param values: author_id, og_author_id, date_time, content, type_of_post
    :return: post_id (Integer)
    """
    try:
        author_id = UsersTableFunctions.get_user_id(values[0])
        og_author_id = UsersTableFunctions.get_user_id(values[1])
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT post_id FROM posts
                        WHERE author_id = ? 
                        AND og_author_id = ? 
                        AND date_time = ?
                        AND content = ?
                        AND type_of_post = ?;""", (author_id, og_author_id, values[2], values[3], values[4], ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_post_author_id(post_id):
    """ returns author_id of a given post
    :param post_id: post_id
    :return: author_id (Integer)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT author_id FROM posts
                        WHERE post_id = ?;""", (post_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_post_og_author_id(post_id):
    """ returns og_author_id of a given post
    :param post_id: post_id
    :return: og_author_id (Integer)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT og_author_id FROM posts
                        WHERE post_id = ?;""", (post_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_post_date_time(post_id):
    """ returns date_time of a given post
    :param post_id: post_id
    :return: date_time (String)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT date_time FROM posts
                        WHERE post_id = ?;""", (post_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_post_content(post_id):
    """ returns the content of a given post
    :param post_id: post_id
    :return: content of the post / may be a link to the picture or video on the server (String)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT content FROM posts
                        WHERE post_id = ?;""", (post_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_type_of_post(post_id):
    """ returns the type of a given post
        1 = content in the form of Text
        2 = content in the form of Picture
        3 = content in the form of Video
    :param post_id: post_id
    :return: type_of_post (Integer)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT type_of_post FROM posts
                        WHERE post_id = ?;""", (post_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


# Checking Functions:


def check_if_post_exists(post_id):
    """ checks if a post already exists
    :param post_id
    :return: post_id (if the post exists) / None if not
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT post_id FROM posts
                        WHERE  post_id = ?;""", (post_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()






