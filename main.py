menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
            },
        "cost":150,
        },
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            },
        "cost":100,
        },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
            },
        "cost":200,
        }
    }
profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100,
    }
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("please insert coins.")
    total=0
    coins_five=int(input("how many 5rs coin?"))
    coins_ten=int(input("how many 10rs coin?"))
    coins_twenty=int(input("how many 20rs coin?"))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total
def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit += coffee_cost
        change=money_received+coffee_cost
        print(f"here is your rs {change} in change.")
        return True
    else:
        print("sorry that's not enough money money refunded.")
        return False
def make_coffee(coffee_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {coffee_name} ☕...enjoy!!")
is_on=True
while is_on:
    choice=input("what would you like to have?(latte/espresso/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}g")
        print(f"money=rs{profit}")
    else:
        coffee_type=menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if  is_payment_successful(payment,coffee_type['cost']):
                 make_coffee(choice,coffee_type['ingredients'])
    
               
           
    

    
    

            
