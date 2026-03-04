grocery=[
{"products" :"Rice",'price':60},
{"products" :"Wheatflour",'price':40},
{"products" :"sugar",'price':45},
{"products" :"dal",'price':140},
{"products" :"tamrid",'price':200},
{"products" :"salt",'price':30},
{"products" :"eggs",'price':180},
{"products" :"milk",'price':10},
{"products" :"tea dust",'price':125},
{"products" :"cooking oil",'price':170} 
]
print ('index'.ljust(6),'product name'.ljust(18),'price'.ljust(19))
index=1
for i in grocery:
    print(str(index).ljust(6),i["products"].ljust(18),str(i["price"]).ljust(19))
    index+=1
bill = 0
new_items = list(map(int,input("enter basket of items:").split()))
print('product name'.ljust(20),'quantity'.ljust(40),'price')
new_items1 = list(set(new_items))
for i in new_items1:
    quantity = new_items.count(i)
    print(grocery[i-1]["products"].ljust(20),str(quantity).ljust(40),grocery[i-1]['price']*quantity)
    bill += grocery[i-1]["price"]* quantity
print(str(bill).center(30))
print ("thank you chossing our! please vist again without failure!")