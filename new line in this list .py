banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f = open("bank .txt","w")
for i in banks_list:
    f.write(i)
    f.write("\n")

