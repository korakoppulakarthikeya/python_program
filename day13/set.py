media= list(input("enter the media withspaces").split())
photos=[]
videos = []
for i in media:
    if i.endswith(".png"):
        photos.append(i)
    else :
        videos.append(i)
print(f"photos:{photos}")
print(f"videos:{videos}")


choice = input("enter if you need to share(yes/no)").lower()
if choice == "yes":
    print(f"photos:{photos}")
    print(f"videos:{videos}")
    selection = set(input("select which file to send: ").split())
    for i in selection:

        if i in photos:
            print(f"{photo} has been sent")
        elif i in videos:
            print(f"{videos} has been sent")
        
        else:
            print('no item has found')
        break
            
elif choice =="no":
    print("thank you")

