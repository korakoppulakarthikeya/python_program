'''try :
    a= int(input())
    print(a[4])
except Exception as e:
    print("error is:",e)
else :
    print('no errror')
finally:
    print("code is executed")'''
try:
    a= int(input())
    if a<0:
        raise Exception("enter th epostive value")
except Exception as e:
    print("exception",e)
else:
    print("final")
finally:
    print("code")