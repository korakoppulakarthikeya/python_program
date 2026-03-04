name = input("enter your name:")
dob = input('enter yuor date of birt [YYY-MM-DD]:')
username = name[:2]+name[-2:]+dob[-2:]+dob[2:4]
print(f"your username is:{username}")