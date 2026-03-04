amount = int(input("enter the amount doess you have:"))

if amount >50000:
    print(f"your amount $: {amount} is appliacble for trip")
elif amount >= 20000:
    print(f"your amount $:{amount} is applicable to go a mall")
elif amount >= 10000:
    print(f"your amount $: {amount} is applicable to buy a gadget")
elif amount >= 5000:
    print(f"your amount $: {amount} is good enough to do kitty part")
else:
    print("you have less amount! please maintain minimum balance")
