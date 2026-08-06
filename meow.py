# I made a combined program of all ideas I had , and i am still working on it and will improve and extend it further. 



import time
import string
import math
import random

def name():
    meow = True
    print("Hello There!")
    print("Welcome to my newbie project.")
    while meow:
        name = input("Please, Tell me what would you like to be called: ").capitalize().strip()
        if not name.isalpha() :
            print("Please, Enter your real name")
            continue
        else:
            meow = False
            return name 

def decision(name):
    meow = True
    print(f"So , {name} What would you like to do ?")
    print(f"1 for bank | 2 for slot machine | 3 for rock_paper_siccors ")
    print(f"4 to eat food | 5 for calculator | 6 to check hunger")
    print(f"7 for weight conversion | 8 for temperature conversion")
    print(f"9 to encrypt msgs | 10 for dice roller | 11 for test")
    print(f"0 to exit the main program")
    time.sleep(1)
    while meow:
        ask = int(input("Please decide : "))
        if ask < 0 or ask > 11 :
            print("Please , choose from the given options")
            continue
        else:
            meow = False
            return ask
            
def bank(user , balance):
    meow = True
    print("Umer's banking program")
    time.sleep(0.5)
    print(f"Welcome {user}")
    while meow:
        print("press 1 to Withdraw | 2 to Deposit | 3 to check Balance | 4 to Exit ")
        option = input("Enter a choice : ").strip()
        if not option.isdigit() :
            print("Please enter a number ")
            continue
        time.sleep(0.5)
        if option == "1" :
            withdraw = float(input("Enter an amount you would like to to withdraw : "))
            if withdraw < 0 or withdraw > balance :
                print("Not valid amount")
                time.sleep(0.5)
                continue
            else:
                print(f"The amount of ${withdraw} has been withdrawn.")
                balance -= withdraw
        elif option == "2" :
            amount =int(input("Enter an amount you would like to deposite : "))
            time.sleep(0.5)
            print(f"You have deposited ${amount} successfully!")
            balance += amount
        elif option =="3":
            time.sleep(1)
            print("*******************************")
            print(f"Your balance is : ${balance}")
            print("*******************************")
            time.sleep(0.25)
        elif option == "4":
            meow = False
            time.sleep(0.25)
            print(f"Thanks for checking in {user}")
            return balance
        else :
            print("Not valid input")
            continue

def slot_machine(user , balance):
    money_won = 0
    money_spent = 0
    bet_won = 0
    spin = 0
    meow = True
    row = []
    bets = []
    a = []
    b = []
    c = []
    faith = {"🍒","🔔","💰","🍌","⭐","🌟"} 
    print(f"Welcome {user}")
    print("**********************************")
    print("🍒","🔔","💰","🍌","⭐","🌟")
    print("**********************************")
    print("Best prize is *🌟|🌟|🌟*")
    while meow:
            bet = input("How much money would you like to bet : $")
            if not bet.isdigit():
                print("Enter a valid amount.")
            bet = int(bet)
            spin +=1
            if bet == 10000:
                meow =False   
            elif bet > balance or bet < 0 :  
                print("Invalid amount")
                continue
            elif bet > 1000:
                print("You have exceeded the limit !")
                continue
            bets.append(bet)
            lowest_bet = min(bets)
            highest_bet = max(bets)
            money_spent += bet
            faith = ["🍒","🔔","💰","🍌","⭐","🌟"]
            row = []
            for _ in range(3):
                row.append(random.choice(faith))
            print(row)
            a == row[0] , b == row[1] , c == row[2]
            if a == b == c:
                bet_won +=1
                if a == "🍒":
                    balance +=   bet * 2
                    money_won += bet * 2
                elif a == "🔔":
                    balance += bet * 3
                    money_won += bet * 3
                elif a == "🍌":
                    balance += bet * 2
                    money_won += bet * 2
                elif a == "🌟":
                    balance += bet * 10
                    money_won += bet * 10
                elif a == "💰":
                    balance += bet * 5
                    money_won += bet * 5
                elif a == "⭐":
                    balance += bet * 7
                    money_won += bet * 7
            elif a == b or b == c or a == c :
                balance -= bet * 0.5
            balance -= bet
            print(f"balance left = ${balance}")
            ask = input("Would you like to spin again ? (y/n/s) : ").lower().strip()
            if ask == "y":
                continue
            elif ask == "s":
                print(f"Spins = {spin}")
                print(f"bets won = {bet_won}")
                print(f"money spent = ${money_spent}")
                print(f"moeny won = ${money_won}")
                print(f"Highest bet = ${highest_bet}")
                print(f"Lowest bet = ${lowest_bet}")
                ask_again = input("Would you like to spin again ? (y/n) : ").lower().strip()
                if ask_again == "y":
                    continue
                else :
                    meow = False
            else:
                meow = False
    return balance            
        
def rock_paper_siccors(user , balance):
    games = 0
    wining_amount = []
    money_won = 0
    win = 0
    meow = True
    options = ("rock","paper","scissors")
    print(f"Welcome {user}")
    print("Before we start.")
    asksss = input("Would you like to give ur opponent a name ? (y/n) : ")
    if asksss == "y":
        comp_name = input("Please assign computer a name : ").capitalize()
        print(f"Thanks you *from {comp_name}*")
    else :
        comp_name = "computer"
        time.sleep(1)
    while meow:
        comp = random.choice(options)
        user_choice = (input("Enter your choice : ")).lower().strip()
        if not user_choice in options :
            print(f"Please Choose from the main three {options}")
            continue
        bet = (input("Enter The amount you would like to bet : ")).strip()
        if not bet.isdigit():
            print("Please Enter an amount ")
            continue
        bet = int(bet)
        if bet == 10000:
            meow = False
        if bet > 1000:
            print("You have exceeded the limit ")
            continue
        elif bet <= 0 or bet > balance :
            print ("Invalid amount")
            continue
        games += 1
        print("---------------------------------")
        print(f"{comp_name:^2} --- {comp:^2}")
        print(f"{user:^2} --- {user_choice:^2}")
        print("---------------------------------")
        if user_choice == "rock" and comp == "scissors" or user_choice == "paper" and comp == "rock" or user_choice == "scissors" and comp  == "paper":
            win += 1
            money_won += bet * 2
            balance += bet * 2
            wining_amount.append(money_won)
            biggest_win = max(wining_amount)
            smallest_win = min(wining_amount)
            print("user won")
            print(balance)
        elif user_choice == comp :
            print("tie")
            print(balance)
        else :
            balance -= bet 
            print("you lose")
            print(balance)
        askes = input("would u like to play again? (y/n/s): ")
        if askes == "y" :
            continue
        elif askes == "s":
            print(f"Games played --- {games}")
            print(f"games won --- {win}")
            print(f"money won --- ${money_won}")
            print(f"Biggest win --- ${biggest_win}")
            print(f"smallest win --- ${smallest_win}")
            print(f"balance --- ${balance}")
            asker = input("would u like to play again? (y/n): ")
            if asker == "y":
                continue
            else:
                meow = False
        else:
            meow = False
    return balance

def order_food(user,balance ,hunger ):
    cart = []
    def TUR():
        meow = True
        total = 0
        foods=["Kebab","Pide","Lahmacun","Baklava","Ayran","Tea"]
        prices = [5.88 , 3.78 , 1.89 , 3.15,0.84,0.53]
        hungers = [ 9 , 7 , 5 , 3 , 2 , 0.5 ]
        print("********************************************")
        print("----------------TURKISH-MENU----------------")
        print("********************************************")
        print(f"{'ITEM/S':<19} | {'PRICE':^10} | {'Hunger':>2}")
        for food , price ,end_hunger in zip(foods , prices ,hungers):
            print(f"{food:<19}   ${price:^8}   {end_hunger:>4}")
        while meow:
                decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                if decide in foods:
                    cart.append(food)
                    decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                elif decide == "N":
                    position = foods.index(food)
                    total = prices[position]
                    meow = False
                    return total
                elif not decide in foods:
                    print("Not a valid option.")
                    continue

    def GER():
        meow = True
        total = 0
        foods=["Schnitzel","Bratwurst","Apfelstrudel","Pretzel","Spezi","Apfelschorle"]
        prices = [16.16 , 5.77 ,6.93 ,3.46,4.62 ,4.62 ]
        hungers = [9,7,4,4,1,1]
        print("********************************************")
        print("----------------GERMAN-MENU-----------------")
        print("********************************************")
        print(f"{'ITEM/S':<19} | {'PRICE':^10} | {'Hunger':>2}")
        for food , price ,end_hunger in zip(foods , prices ,hungers):
            print(f"{food:<19}   ${price:^8}   {end_hunger:>4}")
        while meow:
                decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                if decide in foods:
                    cart.append(food)
                    decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                elif decide == "N":
                    position = foods.index(food)
                    total = prices[position]
                    meow = False
                    return total
                elif not decide in foods:
                    print("Not a valid option.")
                    continue
            
    def ITL():
            meow = True
            total = 0
            foods=["Lasagna","Carbonara","Margherita","Gelato","Chinotto","Espresso"]
            prices = [16.16 ,13.85 ,10.39,4.62 ,3.46,2.31 ]
            hungers = [9,8,7,2,1,0]
            print("********************************************")
            print("----------------ITALIAN-MENU----------------")
            print("********************************************")
            print(f"{'ITEM/S':<19} | {'PRICE':^10} | {'Hunger':>2}")
            for food , price ,end_hunger in zip(foods , prices ,hungers):
                print(f"{food:<19}   ${price:^8}   {end_hunger:>4}")
            while meow:
                    decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                    if decide in foods:
                        cart.append(food)
                        decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                    elif decide == "N":
                        position = foods.index(food)
                        total = prices[position]
                        meow = False
                        return total
                    elif not decide in foods:
                        print("Not a valid option.")
                        continue
            
    def EGY():
            meow = True
            total = 0
            foods=["Koshary","Hawawshi","Ful Medames","Taameya","Karkadeh","Sugarcan juice"]
            prices = [1.61 ,2.21 ,0.80,0.40,0.70 ,0.50]
            hungers = [9,8,7,3,1,2]
            print("********************************************")
            print("--------------EGYPTIAN-MENU----------------")
            print("********************************************")
            print(f"{'ITEM/S':<19} | {'PRICE':^10} | {'Hunger':>2}")
            for food , price ,end_hunger in zip(foods , prices ,hungers):
                print(f"{food:<19}   ${price:^8}   {end_hunger:>4}")
            while meow:
                    decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                    if decide in foods:
                        cart.append(food)
                        decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                    elif decide == "N":
                        position = foods.index(food)
                        total = prices[position]
                        meow = False
                        return total
                    elif not decide in foods:
                        print("Not a valid option.")
                        continue
            
    def PAK():
        meow = True
        total = 0
        foods=["Biryani","Karahi","Tikka","Samosa","Lassi","Chai"]
        prices = [5.00]
        hungers = ["3"]
        print("********************************************")
        print("--------------------menu--------------------")
        print("********************************************")
        print(f"{'ITEM/S':<19} | {'PRICE':^10} | {'Hunger':>2}")
    # I used AI here , to print the code in rows and columns according to how I will.
        for food , price ,end_hunger in zip(foods , prices ,hungers):
            print(f"{food:<19}   ${price:^8}   {end_hunger:>4}")
        while meow:
                decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                if decide in foods:
                    cart.append(food)
                    decide = input("What would you like to order ?('n' to exit) : ").capitalize().strip()
                elif decide == "N":
    # I used AI here because , I just couldn't work with the structure and logic to get the food's price.
                    position = foods.index(food)
                    total = prices[position]
                    meow = False
                    return total
                elif not decide in foods:
                    print("Not a valid option.")
                    continue

    
    amount1 = 0
    amount2 = 0
    amount3 = 0
    amount4 = 0
    amount5 = 0
    meow = True
    print(f"Welcome {user}")
    print("Welcome to 'THE MEOW RESTAURENT'")
    print(f"{user}'s hunger --- {hunger}")
    print(f"{user}'s balance --- {balance}")
    ask = input("Would you like to see the menu ?(y/n) : ").lower().strip()
    if ask == "y":
            while meow:
                asks = input("What Cuisine would you like to eat ?(TUR/ITL/GER/PAK/EGY)('n' to exit)('c' for cart) : ").upper().strip()
                if asks == "TUR" or asks == "1":
                    amount1 = TUR()
                elif asks == "ITL" or asks == "2":
                    amount2 = ITL()
                elif asks == "GER" or asks == "3":
                    amount3 = GER()
                elif asks == "PAK" or asks == "4":
                    amount4 = PAK()
                elif asks == "EGY" or asks == "5":
                    amount5 =  EGY()
                elif asks == "N":
                    meow = False
                    print("Thanks for visiting!")
                elif asks == "C":
                    amount = amount1 + amount2 + amount3 + amount4 + amount5
                    gst = amount * 0.16
                    total = amount + gst
                    print("CART :")
                    print(*cart , sep=" ")
                    print(f"TAX(16%) --- {gst:.2f}")
                    print(f"total --- {total:.2f}")
                    print(f"${balance}") 
                    purchase = str(input("Do you want to buy all of this ?(y/n)('m' for menu) : ")).lower().strip()
                    if purchase == "10000" :
                        meow = False
                    if purchase == "y":
                        if balance < total:
                            print("Insufficient Funds")
                            print("Come again when you will have enough money!")
                            continue
                        elif total ==0 :
                            print("You have bought Nothing")
                        else:
                            balance -= total
                            print("Thanks for making the purchase !!")
                    elif purchase == "m":
                        continue
                    else:
                        meow = False
                else:
                    print("Choose a valid option.")
                    continue
                
    else : 
            print(f"Thanks for visiting! , {user}.")
            return balance

def calculator(user ):
    pass

def eat_food(user , hunger):
    pass

def weight_converter(user):
    pass

def temperature_converter(user):
    pass

def encrypt_msgs(user , balance):
    pass

def dice_roller(user):
    pass

def ball_knowledge(user , knowledge):
    pass

def main():
    meow = True
    knowledge = 0
    balance = 0
    hunger = 0
    print("NOTE : Enter '10000' if you are stuck, If you are not stuck ,It will not work ! ")
    print("NOTE : Your hunger ")
    print("NOTE : If your hunger is 10 ,You cant do anything ,You have to eat food to lower your hunger first")
    print("NOTE : You can check your hunger in order/eat food.")
    time.sleep(4)
    user = name()
    time.sleep(0.2)
    while meow:
        choice = decision(user)
        if choice == 1:
                balance = bank(user , balance)
        elif choice == 2:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                balance = slot_machine(user , balance)
        elif choice == 3:
            if hunger == 10 :
                print("Your hungry")
            else:
                hunger += 1
                balance = rock_paper_siccors(user , balance)
        elif choice == 4:
            balance = order_food(user , balance , hunger)
        elif choice == 5:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                calculator(user)
        elif choice == 6:
            hunger = eat_food(user , hunger)
        elif choice == 7:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                weight_converter(user)
        elif choice == 8:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                temperature_converter(user)
        elif choice == 9:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                encrypt_msgs()
        elif choice == 10:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                balance = dice_roller(user , balance)
        elif choice == 11:
            knowledge = ball_knowledge(user , knowledge)
        else:
            ask_user = input("Are you sure ?(y/n) :")
            if ask_user == "n":
                print("Phew !! , You got me there lad")
                decision(user)
            elif ask_user == "y":
                print("You Died!")
                meow = False
            else:
                print(f"Its a serious matter {user} !")
                ask_user = input("Are you sure ?(y/n) :")

if __name__ == "__main__":
    main()
