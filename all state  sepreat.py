f = open("people.txt","r")
for i in f:
    if "delhi" in i:
        delhi=open("delhi.txt","a")
        delhi.write(i)
    elif "shimla" in i:
        shimla=open("shimla.txt","a")
        shimla.write(i)
    else:
        other=open("other.txt","a")
        other.write(i)
