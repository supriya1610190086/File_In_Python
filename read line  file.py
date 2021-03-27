f = open("people.txt","r")
count=0
for i in f:
    count+=1
    print(count)
f.close()
