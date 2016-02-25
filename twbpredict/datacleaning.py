from sys import argv
script, filename=argv
txt=open(filename,'rw+')
line=txt.readline()
count=0
while len(line)>0:
    attrs=line.split('\t')
    if(len(attrs)<3):
        count=count+1
    line=txt.readline()