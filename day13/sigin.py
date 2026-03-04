details ={
    'korakoppulakarthikeya@gmail.com':'Karthik',
    "achuth@gmail.com":"achuth12",
    "kadirasandeep@gamil.com":'sanddep12'
}
enter_choice = input("signin or signup ").lower()
if enter_choice == 'signup':
    email_id = input("eneter email_id:")
    password = input("enetr password:")
    if email_id in details:
        print("you have already registered")
    else:
        details[email_id]=password
        print("you have registered")
elif enter_choice == 'signin':
    r_emailid= input("enter the email id:")
    r_password = input("eneter the password:")

    if r_emailid in details:
        if r_password == details[r_emailid]:
            print("login sucessful")
        else:
            print("wrong password")
    else:
        print("invalid email")
        
