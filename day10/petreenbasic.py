

"""for i in range(n):#for row 
    for j in range(n):#for column
        print(i,end=" ")
    print()
    0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 """
"""for i in range(n):
    for j in range(n):
        print(num,end=" ")
        num+=1
    print()
    0 1 2 3 4 
4 5 6 7 8 
8 9 10 11 12 
12 13 14 15 16 
16 17 18 19 20 """
"""for i in range(n):
    for j in range(n):
        print(j+i,end=" ")
        num+=1
    print()
    0 1 2 3 4 
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 """
n = int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        if i+j%2==0:
            print(0,end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(n)