nototrious=["kiran","shodhan","rishith"]
names = ["rishith","shodhan","kiran","preetham","max","swasthik","panshu","shreejan","thushar","vidwath"]
score =[2,5,6,8,3,5,6,9,8,2]
for i in range(len(names)):
    if score[i]>5:
        if names[i] not in nototrious:
            print(names[i])
