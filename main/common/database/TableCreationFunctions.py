import sqlite3
from sqlite3 import Error
from . import *


def create_connection():
    """ create a database connection to the SQLite database
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("data.db")
    except Error as e:
        print(e)

    return conn


def create_users_table():
    """ creates the table users if it doesn't exist already
    :return: NONE
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id integer PRIMARY KEY,
                        username text NOT NULL UNIQUE,
                        password text NOT NULL,
                        email text NOT NULL UNIQUE,
                        profile_pic BLOB,
                        color_theme integer,
                        description text);
                      """)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def create_friends_table():
    """ creates the table friends if it doesn't exist already
    :return: NONE
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS friends (
                        friendship_id integer PRIMARY KEY,
                        requester_id integer NOT NULL,
                        receiver_id integer NOT NULL,
                        confirmed integer NOT NULL,
                        FOREIGN KEY (requester_id) REFERENCES users (id),
                        FOREIGN KEY (receiver_id) REFERENCES users (id));
                      """)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def create_posts_table():
    """ creates the table posts if it doesn't exist already
    :return: NONE
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS posts (
                        post_id integer PRIMARY KEY,
                        author_id integer NOT NULL,
                        og_author_id integer NOT NULL,
                        date_time text NOT NULL,
                        content BLOB NOT NULL,
                        type_of_post integer NOT NULL,
                        number_of_likes integer NOT NULL,
                        FOREIGN KEY (author_id) REFERENCES users (id),
                        FOREIGN KEY (og_author_id) REFERENCES users (id));""")
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def create_comments_table():
    """ creates the table posts if it doesn't exist already
    :return: NONE
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS comments (
                        comment_id integer PRIMARY KEY,
                        comm_post_id integer NOT NULL,
                        comm_author_id text NOT NULL,
                        date_time text NOT NULL,
                        comm_content text NOT NULL,
                        FOREIGN KEY (comm_author_id) REFERENCES users (id),
                        FOREIGN KEY (comm_post_id) REFERENCES posts (post_id));""")
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def create_likes_table():
    """ creates the table likes if it doesn't exist already
    :return: NONE
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS likes (
                        like_id integer PRIMARY KEY,
                        like_post_id integer NOT NULL,
                        like_user_id integer NOT NULL,
                        FOREIGN KEY (like_user_id) REFERENCES users (id),
                        FOREIGN KEY (like_post_id) REFERENCES posts (post_id));""")
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()
