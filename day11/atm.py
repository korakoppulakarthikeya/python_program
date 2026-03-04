note=[2000,500,200,100,50,20,10]
amount=int(input("enter amount:"))
for i in note:
    if amount >=i:
        count= amount//i#7570//2000=3
        print(i,"*",count,end=" + ")
        amount = amount%i#7570%2000=1570

if amount!=0:
    print("amount cannot be dispensed")

    

