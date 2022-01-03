def read():
    data = []
    f = open ('Day2\data.txt','r')
    text = f.readlines()
    for line in text:
        data.append(line.split())
    f.close()
    return data

def dive(data):
    j=0
    k=0
    for i in range(len(data)):
        if(data[i][0]=='forward'):
            j+=int(data[i][1])
        elif(data[i][0]=='down'):
            k+=int(data[i][1])
        elif(data[i][0]=='up'):
            k-=int(data[i][1])
    return j*k
    
print(dive(read()))
#read()