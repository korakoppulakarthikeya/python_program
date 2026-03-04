def zero():
    try:
        transaction=[]
        avrage_transctons=sum(transaction)/len(transaction)
    except ZeroDivisionError:
        print("error because the list is empty")
def value():
    try :
        withdrawn_amount = int('10^')
        print("withdraw")
    except ValueError:
        print("value is not int")
def Type():
    try:
        deposit= int(10)+str(10)
    except TypeError:
        print("there inva;lid type")
def Index():
    try:
        transaction_history=[]
        print(transaction_history[4])
    except IndexError:
        print("index out of range")
def key():
    try:
        account={1:"sa"}
        print(account[2])
    except KeyError:
        print("there is a key error")

def file():
    try:
        with open("decode.file",'r')as f:
            data = f.read()
            print(data)    
    except FileNotFoundError:
        print("file not found")
while True:
    print("Atm simulation Menu".center(40,"-"))
    print("1.check  average transaction (ZeroDivisionError)")
    print("2.withdraw with invalid input(valueError)")
    print("3.deposit with invalid data type(TypeError)")
    print("4.Acess deneied transaction History(Indexerror)")
    print("5.Acess non_existent Account(key error)")
    print("6.Read misssing transaction log file(file not found Error)")
    choice= int(input("select an option"))
    if choice <=7:
        if choice == 7:
            break
        elif choice ==1:
            zero()
        elif choice ==2:
            value()
        elif choice ==3:
            Type()
        elif choice ==4:
            Index()
        elif choice ==5:
            key()
        elif choice ==6:
            file()

