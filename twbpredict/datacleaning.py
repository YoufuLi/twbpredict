#there is no need to fill the data. Every line looks good.
#we may need to do something to deal with the dunplication.
import file_operation
import collaborative_filtering
item_file="../resource/item.txt"
train_file="../resource/rec_log_train.txt"
user_key_word_file="../resource/user_key_word.txt"
user_profile_file="../resource/user_profile.txt"

item_matrix=file_operation.readMatrix(item_file)
#test_file=file_operation.readMatrix(test_file)
[train,test]=file_operation.readTrain_Test(train_file)
filename="../resource/rec_log_train.txt"
txt=open(filename,'rw+')
line=txt.readline()
count=0
while len(line)>0:
    attrs=line.split('\t')
    if(len(attrs)!=4):
        count=count+1
    line=txt.readline()
print count