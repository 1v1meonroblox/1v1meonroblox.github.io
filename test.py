

def menu_list():
    menu = ("fudge, brownie, tea, cookie ")
    order = input("this our menu " + menu + "what would you like ")


    

    if order == "fudge":
        golden = input("do you want a golden fudge ? ")
        if golden == "yes":
            price = 30
        else:
            price = 10

    elif order == "brownie" or order == "tea":
        price = 10
    
    elif order == "cookie":
        special = input("do you want a special cookie ? ")
        if special == "yes":
         price = 30
        
    else:
        price = 5
        
    amount = input("good choice picking " + order + " how much would you want ")

    total = int(amount) *  price

    print("your total is £" + str(total) + " thank you coming hope to see you again")

print("welcome to my store")
name = input("what is your name ")
if name == "john":
    status = input("are you old john ")
    if status == "yes":
     print("go away")
     exit()
    else:
        print("oh welcome to the store new john")
        menu_list()

else:
    menu_list()