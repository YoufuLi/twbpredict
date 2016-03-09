import file_operation
import collaborative_filtering
#import networkx as nx
###import net_based_approach as nba
import nba_mysql as nba
item_file="../resource/item.txt"
test_file="../data/testing.txt"
train_file="../resource/rec_log_train.txt"
user_action_file="../resource/user_action.txt"
user_key_word_file="../resource/user_key_word.txt"
user_profile_file="../resource/user_profile.txt"
user_sns_file="../resource/user_sns.txt"
#file_operation.splitTrain_Test(train_file)
#item_matrix=file_operation.readMatrix(item_file)
#####test_matrix=file_operation.readMatrix(test_file)
#print test_matrix
#[train,test]=file_operation.readTrain_Test(train_file)

#user_action=file_operation.readMatrix(user_action_file)
#user_key_word=file_operation.readMatrix(user_key_word_file)
#user_profile=file_operation.readMatrix(user_action_file)
#user_sns=file_operation.readMatrix(user_key_word_file)
#training=file_operation.readMatrix(train_file)
#Rel=nba.CalculateRel('1000002' , '1760423')
#print nba.GetConnectedNodes('1760423')
#print nba.CalculateSim('1000004', '1760423')


# count=0
# for user in test_matrix:
#     recommendations=open('../data/recommendations.txt', 'a')
#     uid=user[0]
#     recommendation=[]
#     recommendation.append(uid)
#     connectedNodes=nba.GetConnectedNodes(uid)
#     for node in connectedNodes:
#         connectivity=nba.GetConnectivity(uid,node)
#         if(connectivity>0.5):
#             recomItems=nba.GetConnectedItems(node)
#             for item in recomItems:
#                 recommendation.append(item)
#     recommendation=''.join(str(e)+'\t' for e in recommendation)
#     recommendations.write(recommendation)
#     recommendations.write('\n')
#     print count
#     count +=1
#     recommendations.close()


print nba.GetConnectedItems('1000004')