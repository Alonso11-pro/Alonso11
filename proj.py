import time


print("----------- Welcome to our restaurant -----------")

#print("---------- Food menu ----------") uk
Foods_menu={ "Pizza"  :30,
             "Burger" :10,
             "Hot dog":15,
             "Donut" :5,
             "Chips" :5}
             
Drink_menu={ "Tea"   :10,
             "Coffee":13,
             "Water" :5,
   "Strawberry juice":25}
is_food=True
is_drink=True
Chosen_foods={}
Chosen_drinks={}
total=0

while is_food:
    print("----------- Food Menu -----------")
    for food,price in Foods_menu.items():
        print(f"{food} : {price}")
    print("---------------------------------")    
    food_choose=input("Type the food you want: ")
    while not food_choose in Foods_menu.keys():
        food_choose=input("You didn't enter a valid value!!Try again: ")
    else:  
        print(f"One piece of {food_choose} will cost you ${Foods_menu.get(food_choose)}")
        food_num=input("How many pieces do you want?: ")
        while not food_num.isdigit():
            food_num=input(" You didn't enter a valid number!! Try again: ")
        else:
            food_num=int(food_num)
            Chosen_foods.update({ food_choose : food_num })
            print(f"You added {food_num} {food_choose} to the cart.")
            no_yes_food=input("Want to add another food? (Y/N): ").upper()
            if no_yes_food=="N":
                is_food=False
            elif no_yes_food=="Y":
                continue
while True:
    Yes_No_drink=input("Want to add a drink? (Y/N): ").upper()
    if Yes_No_drink=="N":
        break
    else:
        while is_drink:
            print("----------- Drink Menu -----------")
            for drink,price in Drink_menu.items():
                print(f"{drink} : {price}")
            print("---------------------------------")    
            drink_choose=input("Type the drink you want: ")
            while not drink_choose.isalpha():
                drink_choose=input("You didn't enter a valid value!!Try again: ")
            else:
                if not drink_choose in Drink_menu.keys():
                    drink_choose=input("You didn't enter a valid value!!Try again: ")
                else:
                    print(f"One piece of {drink_choose} will cost you ${Drink_menu.get(drink_choose)}")
                    drink_num=input("How many pieces do you want?: ")
                    while not drink_num.isdigit():
                        drink_num=input("You didn't enter a valid number!! Try again: ")
                    else:
                        drink_num=int(drink_num)
                        Chosen_drinks.update({ drink_choose : drink_num })
                        print(f"You added {drink_num} {drink_choose} to the cart.")
                        no_yes_drink=input("Want to add another drink? (Y/N): ").upper()
                        if no_yes_drink=="N":
                            is_drink=False
                            
                        elif no_yes_drink=="Y":
                            continue
                        
print("---------- Your cart -----------")
print("Loading your cart", end="",flush=True)
time.sleep(0.5)
print(" . ", end="",flush=True)
time.sleep(0.5)
print(" . ", end="",flush=True)
time.sleep(0.5)
print(" . ", end="",flush=True)
time.sleep(0.5)
print('\n Loaded!')
time.sleep(0.5)

for order_food,order_num in Chosen_foods.items():
    print (f"{order_num} {order_food} : {Foods_menu.get(order_food)}")
    total+=Foods_menu.get(order_food)*order_num
print()
for order_drink,order_num in Chosen_drinks.items():
    print (f"{order_num} {order_drink} : {Drink_menu.get(order_drink)}")
    total+=Drink_menu.get(order_drink)*order_num

print(f"Your toal is ${total}.")
print("------------- Made by: Ali Ahmed --------------")
