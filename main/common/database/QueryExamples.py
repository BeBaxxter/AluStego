# Function Order:
#
# Table Insertion
#
# Table Updating
#
# Table Deletion
#
# Getter Functions
#
# Checking Functions (eg. checking if a friendship exists already)


# Table Entry Value Examples:

user_table_entry1 = 'knoff', '12345', 'knoff@knoff.com', 'linktopic', 0, 'henlo is knoff'
user_table_entry2 = 'baxxter', '12345', 'baxxter@baxxter.com', 'linktoanotherpic', 0, 'henlo is Baxxter'
user_table_entry3 = 'madmax', '12345', 'mad@max.com', 'linktoyetanotherpic', 0, 'henlo is madmax'
user_table_entry4 = 'thatguy', '12345', 'that@guy.com', 'linktoyetanotherpic2', 0, 'henlo is that guy'

friends_table_entry1 = 1, 2
friends_table_entry2 = 3, 2
friends_table_entry3 = 4, 2
friends_table_entry4 = 4, 3
friends_table_entry5 = 1, 3
friends_table_entry6 = 4, 1

posts_table_entry2 = 1, 1, '2021-03-10 10:30', 'My first post!', 1
posts_table_entry1 = 3, 3, '2021-03-10 10:31', 'Max sein Post', 1

comments_table_entry = 1, 2, '2021-03-10 10:31', 'Ayy nice post!'
comments_table_entry2 = 1, 3, '2021-03-10 10:31', 'thx!'
comments_table_entry3 = 2, "knoff", '2021-03-10 10:01', 'HEHE'

like_table_entry1 = 0, 1
like_table_entry2 = 1, 2
like_table_entry3 = 1, 3
like_table_entry4 = 2, 3
like_table_entry5 = 2, 4
like_table_entry6 = 2, 1

# database example for function testing ##########################################################################
#
# create_users_table()
# create_friends_table()
# create_posts_table()
# create_comments_table()
# create_likes_table()
#
#
# insert_new_user(user_table_entry1)
# insert_new_user(user_table_entry2)
# insert_new_user(user_table_entry3)
# insert_new_user(user_table_entry4)
#
#
# insert_new_friendship(friends_table_entry1)
# insert_new_friendship(friends_table_entry2)
# insert_new_friendship(friends_table_entry3)
# insert_new_friendship(friends_table_entry4)
# insert_new_friendship(friends_table_entry5)
# insert_new_friendship(friends_table_entry6)
#
# confirm_friendship(friends_table_entry2)
# confirm_friendship(friends_table_entry5)
# #
# #
# insert_new_post(posts_table_entry1)
# insert_new_post(posts_table_entry2)
#
# insert_new_comment(comments_table_entry)
# insert_new_comment(comments_table_entry2)
# insert_new_like(like_table_entry1)
# insert_new_like(like_table_entry2)
# insert_new_like(like_table_entry3)
# insert_new_like(like_table_entry4)
# insert_new_like(like_table_entry5)
# insert_new_like(like_table_entry6)
