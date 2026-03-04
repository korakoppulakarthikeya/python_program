cart= {}
product ={}
name = input("enter your name :")
while True:
    option = input("enter option A to add product ,B to exit cart").upper()
    if option == 'A':
        product_name = input("enter product name:")
        product_details = input("enter details with specification:")
        product_price = float(input("enter the price of product: "))
        product[product_name]= {
            "product_details":product_details,
            "price":product_price
        }
    elif option == "B":
        print("The products are:")
        print("📦"*50)
        print("product_name".ljust(15," "),"product details".ljust(50," "),"price")
        print("-"*100)
        for v,n in product.items():
    
            print(v.ljust(15," "),product[v]["product_details"].ljust(50,""),product[v]['price'])
        break


while True:
    print(f"{name} welcome")
    if cart:
        print("_"*80)
        print("product_name".ljust(15," "),"quantity".ljust(25," "),"product details")
        print("_"*80)
        for i,j in cart.items():
            
            print(i.ljust(15,' '),":",str(j).ljust(25," "),":",product[i],product[i]['price']*j)
    else:
        print("empty cart🛒")
    print("[A]dd to the cart")
    print("[U]pdate the cart")
    print("[D]elete the product in cart") 
    print("[E]xit from cart")
    choice = input("enter the choice:").upper()
    if choice == "A":
            product_name = input ("enter the product name:")
            items = int(input("enter the no of items"))
            if product_name in product:
                cart[product_name]= items
            else:
                print("product not found ")
    elif choice == "U":
        product_name = input("enter the product:")
        items= int(input("eneter the modified items:"))
        if product_name in cart:
            cart[product_name]= items
        else:
            print(f"{name} you didn't add that product")
    elif choice == "D":
        product_name = input("enetr the product to remove from cart:")
        if product_name in cart:
            cart.pop(product_name)
            print(f"{name}your product has been removed from cart")
        else:
            print(f"{name} ther is no product named {product_name} to delete from cart")
    elif choice == "E":
        print(f"Thank you {name}! keep shooping more🛒")
        break
    
