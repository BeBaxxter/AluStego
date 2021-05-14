import sqlite3
from sqlite3 import Error
#from . import *
from common.database import PostsTableFunctions
from common.database import FriendsTableFunctions
#from common.database import LikesTableFunctions
from common.database import  UsersTableFunctions
from common.database import CommentsTableFunctions
from common.database import  TableCreationFunctions

# Insert Functions:

def insert_new_like(values):
    """ inserts a new like into the database
    :param values: 1.: like_post_id, 2.: like_user_id
    :return: None
    """
    try:
        conn = TableCreationFunctions.create_connection()
        c = conn.cursor()
        post_exists_check = PostsTableFunctions.check_if_post_exists(values[0])
        if post_exists_check == values[0]:
            like_exists_check = check_if_like_exists(values)
            if like_exists_check != values:
                c.execute("""
                    INSERT INTO likes (like_post_id, like_user_id) 
                    VALUES (?, ?);""", values)

                post_id = values[0]
                current_number_of_likes = PostsTableFunctions.get_post_number_of_likes(post_id)
                if current_number_of_likes is not None:
                    new_number_of_likes = current_number_of_likes + 1
                    c.execute(f"""UPDATE posts
                                          SET number_of_likes = ?
                                          WHERE post_id = ?""", (new_number_of_likes, values[0],))

        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Delete Functions:

def delete_like(values):
    """ deletes a given like
    :param values: like_post_id, like_user_id
    :return: None
    """
    try:
        like_id = get_like_id(values)
        post_id = get_like_post_id(like_id)
        if post_id:
            current_number_of_likes = PostsTableFunctions.get_post_number_of_likes(post_id)
            if current_number_of_likes is not None:
                new_number_of_likes = current_number_of_likes - 1
                conn = TableCreationFunctions.create_connection()
                c = conn.cursor()
                c.execute(f"""UPDATE posts
                              SET number_of_likes = ?
                              WHERE post_id = ?""", (new_number_of_likes, post_id))

                c.execute(f"DELETE FROM likes WHERE like_id = ?;", (like_id,))

                conn.commit()
                conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def delete_all_likes_of_user(user_name):
    """ deletes all likes of a given user
    :param user_name: username of the user who's likes shall be deleted
    :return: None
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()

        user_id = UsersTableFunctions.get_user_id(user_name)
        if user_id is not None:
            posts = get_all_post_ids_of_users_likes(user_name)
            if posts is not None:
                for post in posts:
                    current_number_of_likes = PostsTableFunctions.get_post_number_of_likes(post)
                    new_number_of_likes = current_number_of_likes - 1

                    cur.execute(f"""UPDATE posts
                                            SET number_of_likes = ?
                                            WHERE post_id = ?""", (new_number_of_likes, post))

                cur.execute(f"DELETE FROM likes WHERE like_user_id = ?;", (user_id,))

        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Select Functions:

def get_like_id(values):
    """ returns like_id of a given like
    :param values: 1.: like_post_id, 2.: like_user_id
    :return: like_id (Integer in Tuple)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT like_id FROM likes
                        WHERE like_post_id = ? AND like_user_id = ?;""", values)
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


def get_like_post_id(like_id):
    """ returns like_post_id of a given like
    :param like_id: ID of the given Like (Integer)
    :return: like_post_id (Integer in Tuple)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT like_post_id FROM likes
                        WHERE like_id = ? ;""", (like_id, ))
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


def get_like_user_id(like_id):
    """ returns like_user_id of a given like
    :param like_id: ID of the given Like (Integer)
    :return: like_user_id (Integer in Tuple)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT like_user_id FROM likes
                        WHERE like_id = ? ;""", like_id)
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


def get_all_likes_of_user(user_id):
    """ returns all like_id's of a given user
    :param user_id: ID of the user
    :return: Tuple of like_id's (Integer)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT like_id FROM likes
                        WHERE  like_user_id = ?;""", (user_id, ))
        row = cur.fetchall()
        conn.commit()
        conn.close()
        if row:
            tuple_of_like_ids = ()
            for like_id in row:
                tuple_of_like_ids = tuple_of_like_ids + like_id
            if tuple_of_like_ids:
                return tuple_of_like_ids
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_all_post_ids_of_users_likes(user_name):
    """ returns all like_post_id's of a given user
    :param user_name: username of the user
    :return: Tuple of like_post_id's (Integer)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        user_id = UsersTableFunctions.get_user_id(user_name)
        cur.execute(f"""
                        SELECT like_post_id FROM likes
                        WHERE  like_user_id = ?;""", (user_id, ))
        row = cur.fetchall()
        conn.commit()
        conn.close()
        if row:
            tuple_of_like_ids = ()
            for like_id in row:
                tuple_of_like_ids = tuple_of_like_ids + like_id
            if tuple_of_like_ids:
                return tuple_of_like_ids
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


# Checking Functions:

def check_if_like_exists(values):
    """ checks if a like on a given post by a given user already exists
        (checks if the given user has already liked the given post)
    :param values: like_post_id, like_user_id
    :return: values (like_post_id, like_user_id)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT like_post_id, like_user_id FROM likes
                        WHERE  like_post_id = ? AND like_user_id = ?;""", values)
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()