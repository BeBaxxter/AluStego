import sqlite3
from sqlite3 import Error
from . import *

# Insert Functions:


def insert_new_user(values):
    """ inserts one new user entry into the database
        if all uniqueness constraints are met
    :param values: username (String, unique) password, email, profile_pic, color_theme, description
    :return: NONE
    """
    try:
        conn = TableCreationFunctions.create_connection()
        c = conn.cursor()
        c.execute(f"""INSERT INTO users (username, password, email, profile_pic, color_theme, description) 
                      VALUES (?, ?, ?, ?, ?, ?);""", values)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Update Functions:


def update_user_name(user_name, new_user_name):
    """ updates the username of a given user
    :param new_user_name: new name of the user (String)
    :param user_name: old username of the user (String)
    :return: None
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""UPDATE users
                        SET username = ?
                        WHERE id = ?""", (new_user_name, user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def update_user_email(user_name, new_user_email):
    """ updates the email of a given user
    :param new_user_email: new email of the user (String)
    :param user_name: username of the user (String)
    :return: None
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""UPDATE users
                        SET email = ?
                        WHERE id = ?""", (new_user_email, user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def update_user_profile_pic(user_name, link_to_new_pic):
    """ updates the link to the profile picture of a given user
    :param link_to_new_pic: link to the picture to be set as pp on the server (String)
    :param user_name: username of the user (String)
    :return: None
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""UPDATE users
                        SET profile_pic = ?
                        WHERE id = ?""", (link_to_new_pic, user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def update_user_color_theme(user_name, new_user_color_theme):
    """ updates the color theme of a given user
    :param new_user_color_theme: new color theme of the user (String)
    :param user_name: username of the user (String)
    :return: None
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""UPDATE users
                        SET color_theme = ?
                        WHERE id = ?""", (new_user_color_theme, user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def update_user_description(user_name, new_description):
    """ updates the description inside the given user's profile
    :param new_description: (String)
    :param user_name: username of the user (String)
    :return: None
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""UPDATE users
                        SET description = ?
                        WHERE id = ?""", (new_description, user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Delete Functions:

def delete_user(user_name):
    """ deletes a given user including their posts, likes and comments
    :param user_name: username of the user to be deleted
    :return: None
    """
    try:
        user_id = get_user_id(user_name)

        CommentsTableFunctions.delete_all_comments_of_user(user_name)

        post_id_tuple = PostsTableFunctions.get_all_posts_of_user(user_id)
        CommentsTableFunctions.delete_all_comments_of_posts_from_user(post_id_tuple)

        LikesTableFunctions.delete_all_likes_of_user(user_name)

        PostsTableFunctions.delete_all_posts_of_user(user_id)

        FriendsTableFunctions.delete_all_friendships_of_user(user_name)

        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM users WHERE id=?;", (user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Select Functions


def get_user_id(user_name):
    """ returns the user_id of a given user
    :param user_name: username of the user (String)
    :return: user_id (Integer)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT id FROM users 
                        WHERE username = ?""", (user_name,))
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


def get_username(user_id):
    """ returns the username of a given user
    :param user_id: user_id of the user (Integer)
    :return: username (String)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT username FROM users 
                        WHERE id = ?""", (user_id,))
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


def get_user_email(user_name):
    """ returns the email of a given user
    :param user_name: username of the user (String)
    :return: email (String)
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT email FROM users 
                        WHERE id = ?""", (user_id,))
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


def get_user_profile_pic(user_name):
    """ returns the link to the profile picture of a given user
    :param user_name: username of the user (String)
    :return: Link to user's profile picture on the server (String)
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT profile_pic FROM users 
                        WHERE id = ?""", (user_id,))
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


def get_user_color_theme(user_name):
    """ returns the current color_theme of a given user
    :param user_name: username of the user (String)
    :return: current color_theme of a given user (String)
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT color_theme FROM users 
                        WHERE id = ?""", (user_id,))
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


def get_user_description(user_name):
    """ returns the description of the user written in their profile
    :param user_name: username of the user (String)
    :return: description of the user (String)
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT description FROM users 
                        WHERE id = ?""", (user_id,))
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


# Password Functions (IN PROGRESS):

def get_user_hashed_pw(user_name):
    """ returns the hashed value of the user's password to be compared to the input
    :param user_name: username of the user (String)
    :return: hashed value of user password (String)
    """
    try:
        user_id = get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT password FROM users 
                        WHERE id = ?""", (user_id,))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            print(row[0])
            return row[0]
    except Error as e:
        print(e)
        conn.rollback()