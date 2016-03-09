import networkx as nx
import file_operation
item_file="../resource/item.txt"
user_action_file = "../resource/user_action.txt"
user_key_word_file = "../resource/user_key_word.txt"
user_profile_file = "../resource/user_profile.txt"
user_sns_file = "../resource/user_sns.txt"
# user_sns=file_operation.readMatrix(user_sns_file)
# items=file_operation.readMatrix(item_file)
# user_action=file_operation.readMatrix(user_action_file)
# user_key_word=file_operation.readMatrix(user_key_word_file)
# user_profile=file_operation.readMatrix(user_profile_file)
# item_ids=[]
# for _item in items:
#     item_ids.append(_item[0])
def GetConnectedNodes(uid):
    user_sns=file_operation.readMatrix(user_sns_file)
    count = 0
    connectedNodes=[]
    matrix_len = len(user_sns)
    while(count<matrix_len):
        if(uid==user_sns[count][0]):
            connectedNodes.append(user_sns[count][1])
        count=count+1
    return connectedNodes
def GetConnectedItems(uid):
    user_sns=file_operation.readMatrix(user_sns_file)
    items=file_operation.readMatrix(item_file)
    item_ids=[]
    for _item in items:
        item_ids.append(_item[0])
    count = 0
    connectedItems=[]
    matrix_len = len(user_sns)
    while(count<matrix_len):
        if((uid==user_sns[count][0]) and user_sns[count][1] in item_ids):
            connectedItems.append(user_sns[count][1])
        count=count+1
    return connectedItems

def GetConnectivity(uid1,uid2):
    relation=CalculateRel(uid1,uid2)
    interaction=CalculateInt(uid1,uid2)
    similarity=CalculateSim(uid1,uid2)
    connectivity=(relation+interaction+similarity)/2
    return connectivity
def CalculateRel(uid1,uid2):
    user_sns=file_operation.readMatrix(user_sns_file)
    count = 0
    relation = 0
    flag=0
    matrix_len = len(user_sns)
    while(count<matrix_len):
        if((uid1==user_sns[count][0]) & (uid2==user_sns[count][1])):
            flag=flag+1
        if((uid1==user_sns[count][1]) & (uid2==user_sns[count][0])):
            flag=flag+1
        if(flag==2):
            break
        count=count+1
    if(flag==1):
        relation=0.3
    elif(flag==2):
        relation=0.5
    return relation

def CalculateInt(uid1,uid2):
    user_action=file_operation.readMatrix(user_action_file)
    count = 0
    interaction = 0
    matrix_len = len(user_action)
    int_sum=0
    while(count<matrix_len):
        if((uid1==user_action[count][0]) & (uid2==user_action[count][1])):
            num_at=float(user_action[count][2])
            num_retweet=float(user_action[count][3])
            num_comment=float(user_action[count][4])
            int_sum=0.3*num_at+0.4*num_retweet+0.3*num_comment
            break
        count=count+1
    if(int_sum>50):
        interaction=0.5
    elif(int_sum>0):
        interaction=int_sum/100
    else: interaction=0
    return interaction

def CalculateSim(uid1, uid2):
    user_key_word=file_operation.readMatrix(user_key_word_file)
    user_profile=file_operation.readMatrix(user_profile_file)
    count = 0
    flag=0
    similarity = 0.2
    first_user=[]
    second_user=[]
    profile_matrix_len = len(user_profile)
    keyword_matrix_len = len(user_key_word)
    while(count<profile_matrix_len):
        if(uid1==user_profile[count][0]):
            for profile_item in user_profile[count]:
                first_user.append(profile_item)
            flag=flag+1
        if(uid2==user_profile[count][0]):
            for profile_item in user_profile[count]:
                second_user.append(profile_item)
            flag=flag+1
        if(flag==2):
            break
        count=count+1
    count=0
    flag=0
    while(count<keyword_matrix_len):
        if(uid1==user_key_word[count][0]):
            first_user.append(user_key_word[count][1])
            flag=flag+1
        if(uid2==user_key_word[count][0]):
            second_user.append(user_key_word[count][1])
            flag=flag+1
        if(flag==2):
            break
        count=count+1
    if(len(first_user)!=len(second_user) or len(first_user)<6 or first_user[0]==second_user[0]):
        return similarity
    if(first_user[1]!='0-0-' and second_user[1]!='0-0-'):
        if(abs(int(first_user[1])-int(second_user[1]))<10):
            similarity=similarity+0.2
    if(first_user[2]==second_user[2]):
        similarity=similarity+0.2
    if(first_user[4]!=0 and second_user[4]!=0):
        first_user_tags=first_user[4].split(';')
        second_user_tags=second_user[4].split(';')
        for f_tag in first_user_tags:
            for s_tag in second_user_tags:
                if(f_tag==s_tag):
                    similarity=similarity+0.2
    if(len(first_user[5])>0 and len(second_user[5])>0):
        first_user_keywords=first_user[5].split(';')
        second_user_keywords=second_user[5].split(';')
        for f_keyword in first_user_keywords:
            f_keywordArray=f_keyword.split(':')
            if(len(f_keywordArray)==2):
                f_key=f_keywordArray[0]
                f_weight=f_keywordArray[1]
                for s_keyword in second_user_keywords:
                    s_keywordArray=s_keyword.split(':')
                    if(len(s_keywordArray)==2):
                        s_key=s_keywordArray[0]
                        s_weight=s_keywordArray[1]
                        if(f_key==s_key):
                            similarity=similarity+(float(f_weight)+float(s_weight))/2
    if(similarity>1):
        similarity=1
    return similarity