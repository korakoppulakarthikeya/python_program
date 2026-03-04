data = { 
    "karthikeya":{'status':True,'python':90,'sql':89,'apptitude':84},
    "achyuth":{'status':True,'python':95,'sql':56,'apptitude':83},
    "sandeep":{'status':True,'python':40,'sql':70,'apptitude':60},
    "bharath":{'status':False,'python':None,'sql':None,'apptitude':None}
}
user = input ("enter name:")
if user in data:
    if data [user] ['status']:
        sum = data [user] ['python']+ data [user] ['sql'] + data [user] ['apptitude']
        avg = sum/3
        if avg >80:
            print (f"congratulations your avg of marks is :{avg}secured grade A ")
        elif avg >70:
            print (f"congratulations your avg of marks is :{avg}secured grade B ")
        elif avg >60:
            print (f"congratulations your avg of marks is :{avg}secured grade C")
        elif avg >50:
            print (f"congratulations your avg of marks is :{avg}secured grade D")
        else:
            print(f"your avg is {avg} ! you got failed work hard")

    else :
        print(f"your are absent")   
else:
    print(f"your unable to fetch")