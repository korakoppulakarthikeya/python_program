def add(a,b):
    return a+b
def multiply (a,b):
    return a*b
def subtraction (a,b):
    return a-b
def division (a,b):
    return a/b
def modulus (a,b):
    return a%b
expression = input("enter expression to calculate:")
for i in expression:
    if i == '+':
        a,b = expression.split('+')
        
        print(add(int(a),int(b)))
    elif i == '-':
        a,b = expression.split('-')
        print(subtraction(int(a),int(b)))
    elif i == '*':
        a,b = expression.split('*')
        print(multiply(int(a),int(b)))
    elif i == '%':
        a,b = expression.split('%')
        print(mod (int(a),int(b)))
    elif i == '/':
        a,b = expression.spli('/')
        print(division(int(a),int(b)))
    else:
        print("invalid operation")


    


