passswords = input("enter your password:")
if len(passswords) >=4:
    s = set()
    for i in passswords:
        if i.isupper():
            s.add("capitial letters")
        elif i.islower():
            s.add("lower letters")
        elif i.isdigit():
            s.add("numeric")
        else:
            s.add("special char")
else:
    print("plaese select min number of character(4)")
if len(s)== 4:
    print("strong password👌🏻",passswords)
else:
    print("oops! you have enter a weak password please retry it again☹️")