import sqlite3
from sqlite3 import Error
#from . import *

from common.database import PostsTableFunctions
#from common.database import FriendsTableFunctions
from common.database import LikesTableFunctions
from common.database import  UsersTableFunctions
from common.database import CommentsTableFunctions
from common.database import  TableCreationFunctions

# Insert Functions:

def insert_new_friendship(values):
    """ inserts one friendship entry into the database
        checks if the given friendship is un-confirmed (unconfirmed_check)
        checks if the given friendship is confirmed (confirmed_check)
    :param values: usernames of requester and receiver as Strings eg.: "name1", "name2"
    :return: NONE
    """
    try:
        requester_id = UsersTableFunctions.get_user_id(values[0])
        receiver_id = UsersTableFunctions.get_user_id(values[1])
        values_tuple = (requester_id, receiver_id)

        unconfirmed_check = check_for_unconfirmed_friendship(values)

        confirmed_check = check_for_confirmed_friendship(values)

        if unconfirmed_check != values_tuple and confirmed_check != values_tuple:
            requester_id = UsersTableFunctions.get_user_id(values[0])
            receiver_id = UsersTableFunctions.get_user_id(values[1])
            conn = TableCreationFunctions.create_connection()
            c = conn.cursor()
            c.execute(f"""
                    INSERT INTO friends (requester_id, receiver_id, confirmed) 
                    VALUES (?, ?, 0);""", (requester_id, receiver_id, ))
            conn.commit()
            conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Update Functions:

def confirm_friendship(values):
    """ confirms one existing friendship entry (sets confirmed = 1)
        checks if the given friendship is un-confirmed (unconfirmed_check)
        gets friendship id based on the user_id's from param: values
    :param values: usernames of requester and receiver as Integers
    :return: NONE
    """
    try:
        checked_requester_id = UsersTableFunctions.get_user_id(values[0])
        checked_receiver_id = UsersTableFunctions.get_user_id(values[1])
        checked_values_tuple = (checked_requester_id, checked_receiver_id)

        requester_id = UsersTableFunctions.get_user_id(values[0])
        receiver_id = UsersTableFunctions.get_user_id(values[1])
        values_tuple = (requester_id, receiver_id)

        friendship_id = get_friendship_id(values)
        if friendship_id is not None:
            if checked_values_tuple == values_tuple:
                try:
                    conn = TableCreationFunctions.create_connection()
                    c = conn.cursor()
                    c.execute(f"""
                                    UPDATE friends
                                    SET confirmed = 1
                                    WHERE friendship_id = ?;""", friendship_id)
                    conn.commit()
                    conn.close()
                except Error as e:
                    print(e)
                    conn.rollback()
    except Error as e:
        print(e)
        conn.rollback()


# Delete Functions:

def delete_confirmed_friendship(values):
    """ deletes one friendship entry from the database
        checks if a friendship is confirmed (confirmed_check)
        gets friendship id based on the requester and receiver names from param: values
    :param values: usernames of requester and receiver as Integers
    :return: NONE
    """
    try:
        confirmed_check = check_for_confirmed_friendship(values)

        checked_requester_id = UsersTableFunctions.get_user_id(values[0])
        checked_receiver_id = UsersTableFunctions.get_user_id(values[1])
        checked_values_tuple = (checked_requester_id, checked_receiver_id)

        if checked_values_tuple == confirmed_check:
            try:
                friendship_id = get_friendship_id(values)
                conn = TableCreationFunctions.create_connection()
                c = conn.cursor()
                c.execute(f"""  
                                DELETE FROM friends 
                                WHERE friendship_id = ?;""", friendship_id)
                conn.commit()
                conn.close()
            except Error as e:
                print(e)
                conn.rollback()
    except Error as e:
        print(e)
        conn.rollback()


def delete_unconfirmed_friendship(values):
    """ deletes one friendship entry from the database
        eg. if a user declines a friend invite
        checks if the friendship is unconfirmed (unconfirmed_check)
        gets friendship id based on the requester and receiver names from param: values
    :param values: usernames of requester and receiver as Integers
    :return: NONE
    """
    try:
        unconfirmed_check = check_for_unconfirmed_friendship(values)

        checked_requester_id = UsersTableFunctions.get_user_id(values[0])
        checked_receiver_id = UsersTableFunctions.get_user_id(values[1])
        checked_values_tuple = (checked_requester_id, checked_receiver_id)

        if checked_values_tuple == unconfirmed_check:
            try:
                friendship_id = get_friendship_id(values)
                conn = TableCreationFunctions.create_connection()
                c = conn.cursor()
                c.execute(f"""  
                                DELETE FROM friends 
                                WHERE friendship_id = ?;""", friendship_id)
                conn.commit()
                conn.close()
            except Error as e:
                print(e)
                conn.rollback()
    except Error as e:
        print(e)
        conn.rollback()


def delete_all_friendships_of_user(user_name):
    """ deletes all friendship entries of a user from the database
    :param user_name: username of the user who's friendships shall be deleted
    :return: NONE
    """
    try:
        user_id = UsersTableFunctions.get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        c = conn.cursor()
        c.execute(f"""  
                        DELETE FROM friends 
                        WHERE requester_id = ?;""", (user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()

    try:
        conn = TableCreationFunctions.create_connection()
        c = conn.cursor()
        c.execute(f"""  
                        DELETE FROM friends 
                        WHERE receiver_id = ?;""", (user_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Select Functions:

def get_all_friends_ids(user_name):
    """ returns a tuple including all user_id's of confirmed friends of given user
    :param user_name: username of User
    :return: Tuple (user_id_of_friend_1, user_id_of_friend_2, ...,)
    """
    try:
        user_id = UsersTableFunctions.get_user_id(user_name)
        friends_list = []
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()

        cur.execute(f"""SELECT receiver_id FROM friends GROUP BY confirmed, requester_id, receiver_id
                        HAVING confirmed=1 AND requester_id= ?""", (user_id, ))
        rows1 = cur.fetchall()
        if rows1:
            friends_list.append(rows1)

        cur.execute(f"""SELECT requester_id FROM friends GROUP BY confirmed, requester_id, receiver_id 
                        HAVING confirmed=1 AND receiver_id= ?""", (user_id, ))
        rows2 = cur.fetchall()
        if rows2:
            friends_list.append(rows2)

        conn.commit()
        conn.close()

        if rows1 or rows2:
            friends_tuple = ()
            for friends in friends_list:
                for friend in friends:
                    friends_tuple = friends_tuple + friend
            return friends_tuple
        else:
            return None

    except Error as e:
        print(e)
        conn.rollback()


def get_all_unconfirmed_friends_ids(user_name):
    """ returns a tuple including all user_id's of unconfirmed friends of given user
    :param user_name: username of User
    :return: Tuple (user_id_of_friend_1, user_id_of_friend_2, ...,)
    """
    try:
        user_id = UsersTableFunctions.get_user_id(user_name)
        unconfirmed_friends_list = []
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()

        cur.execute(f"""SELECT receiver_id FROM friends GROUP BY confirmed, requester_id, receiver_id
                        HAVING confirmed=0 AND requester_id= ?""", (user_id, ))
        rows1 = cur.fetchall()
        if rows1:
            unconfirmed_friends_list.append(rows1)

        cur.execute(f"""SELECT requester_id FROM friends GROUP BY confirmed, requester_id, receiver_id 
                        HAVING confirmed=0 AND receiver_id= ?""", (user_id, ))
        rows2 = cur.fetchall()
        if rows2:
            unconfirmed_friends_list.append(rows2)

        conn.commit()
        conn.close()

        if rows1 or rows2:
            unconfirmed_friends_tuple = ()
            for friend in unconfirmed_friends_list[0]:
                unconfirmed_friends_tuple = unconfirmed_friends_tuple + friend
            return unconfirmed_friends_tuple
        else:
            return None

    except Error as e:
        print(e)
        conn.rollback()


def get_friendship_id(values):
    """ returns the friendship_id of the two given users
    :param values: usernames of requester and receiver as Integers
    :return: friendship_id (Integers in Tuple)
    """
    try:
        requester_id = UsersTableFunctions.get_user_id(values[0])
        receiver_id = UsersTableFunctions.get_user_id(values[1])
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT friendship_id FROM friends
                        WHERE  requester_id = ? AND receiver_id = ?;""", (requester_id, receiver_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row
    except Error as e:
        print(e)
        conn.rollback()


# Checking Functions:

def check_for_unconfirmed_friendship(values):
    """ checks if a friendship given by values of two user_id's is unconfirmed
    :param values: usernames of user1 and user2 as Integers
    :return: NONE
    """
    try:
        requester_id = UsersTableFunctions.get_user_id(values[0])
        receiver_id = UsersTableFunctions.get_user_id(values[1])
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                    SELECT requester_id, receiver_id FROM friends
                    WHERE  requester_id = ? AND receiver_id = ?
                    AND confirmed = 0;""", (requester_id, receiver_id, ))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row
    except Error as e:
        print(e)
        conn.rollback()


def check_for_confirmed_friendship(values):
    """ checks if a friendship given by values of two user_id's is confirmed
    :param values: usernames of requester and receiver as Integers
    :return: values (if confirmed = 1) or NONE (if unconfirmed)
    """
    try:
        requester_id = UsersTableFunctions.get_user_id(values[0])
        receiver_id = UsersTableFunctions.get_user_id(values[1])
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                            SELECT requester_id, receiver_id FROM friends
                            WHERE  requester_id = ? AND receiver_id = ?
                            AND confirmed = 1;""", (requester_id, receiver_id,))
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
