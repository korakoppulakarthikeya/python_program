Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input("enter your name")
enter your namekarthikeya
>>> 
>>> mobile_no = int(input("enter your contact number:"))
enter your contact number:9398688270
>>> product_1 = input("enter product you have purchased:")
enter product you have purchased:milk
>>> price_1 = int(input ("enter the price of the product_1 :"))
enter the price of the product_1 :40
>>> product_2 = input("enter product you have purchased:")
enter product you have purchased:bread
>>> price_2 = int(input ("enter the price of the product_2 :"))
enter the price of the product_2 :79
>>> product_3 = input("enter product you have purchased:")
enter product you have purchased:peanut butter
>>> 
... price_2 = int(input ("enter the price of the product_2 :"))
enter the price of the product_2 :80
>>> 
... price_3 = int(input ("enter the price of the product_3 :"))
enter the price of the product_3 :300
>>> print(f"{name} your bill\n The items you have purchased")
karthikeya your bill
 The items you have purchased
>>> print(f"{product_1}:{price_1}\n,{product_2}:{price_2}\n,{product_3}:{price_3}")
milk:40
,bread:80
,peanut butter:300
>>> total_bill = price_1+price_2+price_3
>>> print(f"your total bill is {total_bill}\n ...please visit again...")
your total bill is 420
 ...please visit again...
