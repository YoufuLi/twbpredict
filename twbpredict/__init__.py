import file_operation
import collaborative_filtering
item_file="../resource/item.txt"
test_file="../resource/rec_log_test.txt"
train_file="../resource/rec_log_train.txt"
user_action_file="../resource/user_action.txt"
user_key_word_file="../resource/user_key_word.txt"
user_profile_file="../resource/user_profile.txt"
user_sns_file="../resource/user_sns.txt"
item_matrix=file_operation.readMatrix(item_file)
#test_file=file_operation.readMatrix(test_file)
[train,test]=file_operation.readTrain_Test(train_file)

print len(train)
print len(test)
#user_action=file_operation.readMatrix(user_action_file)
#user_key_word=file_operation.readMatrix(user_key_word_file)
#user_profile=file_operation.readMatrix(user_action_file)
#user_sns=file_operation.readMatrix(user_key_word_file)