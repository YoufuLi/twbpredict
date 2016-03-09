import random
#this method read the file, and return a two dimension array
def readMatrix(filename):
    txt=open(filename,'rw+')
    line=txt.readline()
    count=0
    matrix=[]
    while len(line)>0:
        attrs=line.strip("\n").split('\t')
        matrix.append(attrs)
        count+=1
        line=txt.readline()
    txt.close()
    return matrix


#this method get the traning and testing dataset from 'rec_log_train.txt'
def splitTrain_Test (filename):
    txt = open(filename, 'rw+')
    testing = open('../data/testing.txt', 'w')
    training = open('../data/training.txt', 'w')
    line = txt.readline()
    count = 0
    train_matrix = []
    test_matrix = []
    while len(line) > 0 and count<100:
        #attrs=line.strip("\n").split('\t')
        if(random.random()>=0.7):
            testing.write(line)
            #test_matrix.append(attrs)
        else:
            training.write(line)
            #train_matrix.append(attrs)
        count += 1
        line = txt.readline()
    txt.close()
    #return [train_matrix, test_matrix]