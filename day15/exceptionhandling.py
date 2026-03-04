try :
    if a >10:
        print("value is greater")
except (NameError,TypeError,ValueError) as e:#zerodevisionerror , value error,indexerror
    print(f'a is not defined{e}')
except IndexError:#
    print("type is not defined")
else:
    print('code is clean')
finally:
    print("code is executed")