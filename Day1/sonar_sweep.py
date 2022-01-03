def sonar(data):
    j=0
    for i in range(len(data)-1):
        if(data[i+1]>data[i]):
            j+=1
    return j

def read():
    data = []
    f = open ('Day1\data.txt','r')
    text = f.readlines()
    for line in text:
        data.append(int(line.strip()))
    f.close()
    return data

#count = sonar([199,200,208,210,200,207,240,269,260,263])
count = sonar(read())
print(count)