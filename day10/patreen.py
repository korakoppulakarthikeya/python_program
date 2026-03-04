'''n= int(input("enter the number:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
    * * * * * 
* * * * 
* * * 
* * 
* '''
'''n = int(input("enter the number:"))
for i in range(n):
    for spec in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
        * 
      * * 
    * * * 
  * * * * 
* * * * * '''
'''n = int(input("enter the number:"))
for i in range(n):
    for spec in range():
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()'''

n = int(input("enter  the size:"))
for row in range(n*2):
    if row <=n:
        print("*"*(row+1))
        
