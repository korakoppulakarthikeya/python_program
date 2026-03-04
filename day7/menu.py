data = {
    9847:{'pin':6547,'balance':20000,'Transaction_history':[]},
    1267:{'pin':8942,'balance':13000,'Transaction_history':[]},
    7563:{'pin':4321,'balance':7000,'Transaction_history':[]},
    1433:{'pin':9042,'balance':650,'Transaction_history':[]}
}
acc_no = int(input("enter account no:"))
pin = int(input("enter pin no:"))
def check_balance():
    print(f"your current a/c balance is : {data[acc_no]['balance']}")

def withdraw_amount():
    withdraw = int(input("enter amount withdraw amount:"))
    if data [acc_no] ['balance'] > withdraw:
        print(f"The amount after withdrawl : { data[acc_no]['balance'] - withdraw}")
        data[acc_no]["Transaction_history"].append(withdraw)
    else:
        print(f"insuffcient funds ! please maintain sufficient balance")
def deposit(balance):
    deposit = int(input("enter amount to deposit:"))
    balance += deposit
    data[acc_no]["Transaction_history"].append(deposit)
    print(f"The balance after depositing:{balance} ")
def transactions():
    print(f"yourtansaction history is :\n{data[acc_no]["Transaction_history"]}")
def new_pin_gen():
    new_pin = int(input("enter new pin:"))
    data [acc_no] ['pin'] = new_pin
    print("pin changed sucessfully")
flag = True
while flag:
    if acc_no in data and data[acc_no]['pin']== pin:
        print(f"1.check balanace\n 2. witdraw amount\n 3.deposit amount\n 4. transaction history\n 5.change pin\n 6.exit")
        choice = int(input("enter your choice:"))
        if choice == 1:
            check_balance()
        if choice == 2:
            withdraw_amount()
        if choice ==3:
            deposit(data[acc_no]['balance'])
        if choice == 4 :
            transactions ()
        if choice == 5:
            new_pin_gen()
            break

        if choice == 6 :
            flag = False
            print("thank you visit agaain")
    else :
        print (f"entered wrong account number")
        break
    
