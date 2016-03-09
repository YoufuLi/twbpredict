LOAD DATA LOCAL INFILE '/Users/youfuli/PycharmProjects/twbpredict/resource/item.txt' INTO TABLE item
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(item_id, item_cat, item_key_word);

LOAD DATA LOCAL INFILE '/Users/youfuli/PycharmProjects/twbpredict/resource/user_action.txt' INTO TABLE user_action
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(from_uid, to_uid, at_num,retweet_num,comment_num);

LOAD DATA LOCAL INFILE '/Users/youfuli/PycharmProjects/twbpredict/resource/user_key_word.txt' INTO TABLE user_key_word
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(uid, key_word);

LOAD DATA LOCAL INFILE '/Users/youfuli/PycharmProjects/twbpredict/resource/user_profile.txt' INTO TABLE user_profile
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(uid, user_year, user_sex,tweet_num,user_tags);

LOAD DATA LOCAL INFILE '/Users/youfuli/PycharmProjects/twbpredict/resource/user_sns.txt' INTO TABLE user_sns
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
(follower_uid, followee_uid);

