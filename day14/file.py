''''with open("/Users/codegnan/day14/intro.txt","r") as file:

    introduction = file.read()
    print(introduction)'''
'''f = open("/Users/codegnan/day14/intro.txt","r")
inro = f.read()
f.seek(0)
intro2 = f.readline()
f.seek(0)
intro3 = f.readlines()
f.close()
print(inro,intro2,intro3,sep="\n\n")'''