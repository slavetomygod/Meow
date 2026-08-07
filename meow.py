# I made a combined program of all ideas I had , and i am still working on it and will improve and extend it further. 

import time
import string
import math
import random
bag = []
cash =round(1000,2)
balance =round(0,2)
money_spent =round(0,2)
money_made =round(0,2)
knowledge = 0
hunger = 0
ball_knowledge_lock = False

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
    print(f"4 to eat food | 5 for calculator | 6 to order food")
    print(f"7 for weight conversion | 8 for temperature conversion")
    print(f"9 to encrypt msgs | 10 for dice roller | 11 for test")
    print(f"12 for stats | 0 to exit the main program")
    time.sleep(1)
    while meow:
        ask = input("Please decide : ")
        if not ask.isdigit():
            print("Enter a valid option")
            continue
        ask = int(ask)
        if ask < 0 or ask > 12 :
            print("Please , choose from the given options")
            continue
        else:
            meow = False
            return ask
            
def bank(user):
    global cash
    global balance
    meow = True
    print("Umer's banking program.")
    time.sleep(0.5)
    print(f"Welcome {user}!")
    while meow:
        print("press 1 to Withdraw | 2 to Deposit | 3 to check Balance | 4 to Exit ")
        option = input("Enter a choice : ").strip()
        if not option.isdigit() :
            print("Please enter a number.")
            continue
        time.sleep(0.5)
        if option == "1" :
            withdraw = input("Enter an amount you would like to to withdraw : ").strip()
            if not withdraw.isdigit():
                print("Enter a valid amount.")
                continue
            withdraw = float(withdraw)
            if withdraw <= 0 or withdraw > balance :
                print("Not valid amount.")
                time.sleep(0.5)
                continue
            else:
                print(f"The amount of ${withdraw} has been withdrawn.")
                balance -= withdraw
                cash += withdraw
        elif option == "2" :
            ask = input("Enter an amount you would like to deposite : ")
            if not ask.isdigit():
                print("Enter a valid amount !")
                continue
            ask = float(ask)
            if ask <= 0 or ask > cash:
                print("You dont have enough cash to make that deposite!")
                continue
            print(f"You have deposited ${ask} successfully!")
            cash -= ask
            balance += ask
        elif option =="3":
            time.sleep(1)
            print("*******************************")
            print(f"Your balance is : ${balance}")
            print("*******************************")
            time.sleep(0.25)
        elif option == "4":
            meow = False
            time.sleep(0.25)
            print(f"Thanks for checking in {user}!")
            return 
        else :
            print("Not valid input.")
            continue

def slot_machine(user):
    global cash
    global money_made
    global money_spent
    money_won = 0
    money_spent_on_stakes = 0
    bet_won = 0
    spin = 0
    meow = True
    row = []
    stakes = []
    symbols = {"🍒","🔔","💰","🍌","⭐","🌟"} 
    print(f"Welcome {user}")
    print("**********************************")
    print("🍒","🔔","💰","🍌","⭐","🌟")
    print("**********************************")
    print("Best prize is *🌟|🌟|🌟*")
    while meow:
            stake = input("How much money would you like to bet ('n' to exit: $").lower()
            if stake == "n":
                return
            if not stake.isdigit():
                print("Enter a valid amount.")
                continue
            stake = int(stake)
            spin +=1
            if stake == 10000:
                return 
            elif stake > cash or stake < 0 :  
                print("Invalid amount")
                continue
            elif stake > 1000:
                print("You have exceeded the limit !")
                continue
            money_spent += stake
            stakes.append(stake)
            lowest_bet = min(stakes)
            highest_bet = max(stakes)
            money_spent_on_stakes += stake
            for _ in range(3):
                row.append(random.choice(symbols))
            print(row)
            if row[0] == row[1] == row[2]:
                bet_won +=1
                if row[0] == "🍒":
                    cash +=   stake * 2
                    money_won += stake 
                    money_made += stake 
                elif row[0] == "🔔":
                    cash += stake * 3
                    money_won += stake * 2
                    money_made  += stake * 2
                elif row[0] == "🍌":
                    cash += stake * 2
                    money_won += stake 
                    money_made += stake 
                elif row[0] == "🌟":
                    cash += stake * 10
                    money_won += stake * 9
                    money_made += stake * 9
                elif row[0] == "💰":
                    cash += stake * 5
                    money_won += stake *4
                    money_made += stake *4
                elif row[0] == "⭐":
                    cash += stake * 7
                    money_won += stake * 6
                    money_made += stake * 6
            elif row[0] == row[1]  or row[1]  == row[2] or row[0] == row[2] :
                cash -= stake * 0.5
            cash -= stake
            print(f"balance left = ${cash}")
            ask = input("Would you like to spin again ? (y/n/s) : ").lower().strip()
            if ask == "y":
                continue
            elif ask == "s":
                print(f"Spins = {spin}")
                print(f"bets won = {bet_won}")
                print(f"money spent = ${money_spent_on_stakes}")
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
    return          
        
def rock_paper_siccors(user):
    global cash
    global money_spent
    global money_made
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
        bet = (input("Enter The cash you would like to bet : ")).lower().strip()
        if bet == "n":
            return
        if not bet.isdigit():
            print("Please Enter an amount ")
            continue
        bet = int(bet)
        if bet == 10000:
            return
        if bet > 1000:
            print("You have exceeded the limit ")
            continue
        elif bet <= 0 or bet > cash :
            print ("Invalid cash")
            continue
        money_spent += bet
        games += 1
        print("---------------------------------")
        print(f"{comp_name:^2} --- {comp:^2}")
        print(f"{user:^2} --- {user_choice:^2}")
        print("---------------------------------")
        if user_choice == "rock" and comp == "scissors" or user_choice == "paper" and comp == "rock" or user_choice == "scissors" and comp  == "paper":
            win += 1
            money_won += bet 
            money_made += bet
            cash += bet * 2
            wining_amount.append(money_won)
            biggest_win = max(wining_amount)
            smallest_win = min(wining_amount)
            print("user won")
            print(cash)
        elif user_choice == comp :
            print("tie")
            print(cash)
        else :
            cash -= bet 
            print("you lose")
            print(cash)
        askes = input("would u like to play again? (y/n/s): ")
        if askes == "y" :
            continue
        elif askes == "s":
            print(f"Games played --- {games}")
            print(f"games won --- {win}")
            print(f"money won --- ${money_won}")
            print(f"Biggest win --- ${biggest_win}")
            print(f"smallest win --- ${smallest_win}")
            print(f"balance --- ${cash}")
            asker = input("would u like to play again? (y/n): ")
            if asker == "y":
                continue
            else:
                meow = False
        else:
            meow = False
    return cash

def order_food(user ,hunger ):
    global cash
    global money_spent
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
        prices = [1.30 , 4.50 , 0.80 , 0.15 , 0.89 , 0.34]
        hungers = [7 , 9 , 5, 3, 4,1]
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

    amount = 0
    amount1 = 0
    amount2 = 0
    amount3 = 0
    amount4 = 0
    amount5 = 0
    meow = True
    print(f"Welcome {user}")
    print("Welcome to 'THE MEOW RESTAURENT'")
    print(f"{user}'s hunger --- {hunger}")
    print(f"{user}'s balance --- {cash}")
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
                    print(f"${cash}") 
                    purchase = input("Do you want to buy all of this ?(y/n)('m' for menu) : ").lower().strip()
                    if purchase == 10000 :
                        return
                    if purchase.isdigit:
                        print("Make a choice from the mentioned!")
                        continue
                    if purchase == "y":
                        if cash < total:
                            print("Insufficient Funds")
                            print("Come again when you will have enough money!")
                            continue
                        elif total ==0 :
                            print("You have Nothing in your cart.")
                        else:
                            cash -= total
                            print(f"Thanks for making the purchase !!")
                    elif purchase == "m":
                        continue
                    else:
                        meow = False
                else:
                    print("Choose a valid option.")
                    continue            
    else : 
            print(f"Thanks for visiting! , {user}.")
            bag.append(cart)
            return 

def calculator(user):
    pass

def eat_food(user):
    global hunger

def weight_converter(user):
    pass

def temperature_converter(user):
    pass

def encrypt_msgs(user):
    pass

def dice_roller(user):
    pass

def ball_knowledge(user):
    knowledge = 0
    global ball_knowledge_lock
    if ball_knowledge_lock == False:
        print("You have already given the test once ou cant give it again.")
        return
    print(f"Welcome {user}, Just a reminder that after this you cant retake the test!")
    time.sleep(2)
    questions = [
        "How many days are there in a normal year?",
        "Which planet is known as the 'Red Planet'?",
        "What is the largest ocean on Earth?",
        "Which animal is known as the 'Ship of the Desert'?",
        "How many colors are there in a rainbow?",
        "What is the capital city of France?",
        "Which gas do humans need to breathe in to survive?",
        "Which country is famous for the Pyramids?",
        "What is the hardest natural substance on Earth?",
        "How many legs does a spider have?",
        "Which country has won the Second most FIFA World Cups?",
        "Best midfield Player ?",
        "Which player has the most own goals ?",
        "Famous Brazilian legend?",
        "Who is often considered the greatest player?",
    ]
    options = [
        ("A) 300", "B) 365", "C) 366", "D) 400"),
        ("A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"),
        ("A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"),
        ("A) Horse", "B) Camel", "C) Elephant", "D) Lion"),
        ("A) 5", "B) 6", "C) 7", "D) 8"),
        ("A) London", "B) Berlin", "C) Rome", "D) Paris"),
        ("A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"),
        ("A) India", "B) Egypt", "C) Mexico", "D) China"),
        ("A) Gold", "B) Iron", "C) Diamond", "D) Wood"),
        ("A) 6", "B) 8", "C) 10", "D) 12"),
        ("A) Brazil", "B) Germany", "C) Argentina", "D) France"),
        ("A) Zidane", "B) Ozil", "C) KDB", "D) Modric"),
        ("A) Ronaldo", "B) Messi", "C) Neymar Jr", "D) Suarez"),
        ("A) Zico", "B) Kaka", "C) Ronaldinho", "D) KDB"),
        ("A) Ronaldo", "B) Messi", "C) Pele", "D) Maradona"),
    ]
    answers = [
        "B","B","C","B","C","D","A","B","C","B",
        "B","B","A","A","B",
    ]
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question}")
        if i >= len(options) or i >= len(answers):
            print("Question data incomplete; skipping.")
            continue
        for opt in options[i]:
            print(opt)
        while True:
            ask = input("Enter an option (A/B/C/D): ").upper().strip()
            if ask not in ("A","B","C","D"):
                print("Not a valid option")
                continue
            break
        if ask == answers[i]:
            print("Correct!")
            knowledge += 1
        else:
            print(f"Wrong. Correct answer: {answers[i]}")
    print(f"\nYou scored {knowledge}/{len(questions)}")
    return knowledge

def stats(user):
    global cash
    global balance
    global hunger
    global knowledge
    print(f"Player name -- {user}")
    print(f"Cash -- {cash}")
    print(f"Balnce -- {balance}")
    print(f"hunger -- {hunger}",)
    print(f"Money made -- {money_made}",)
    print(f"Money spent -- {money_spent}",)
    print(f"Knowledge -- {knowledge}")

def main():
    global knowledge
    global hunger
    meow = True
    print("NOTE : Enter '10000' if you are stuck, If you are not stuck ,It will not work ! ")
    print("NOTE : Your hunger ")
    print("NOTE : If your hunger is 10 ,You cant do anything ,You have to eat food to lower your hunger first")
    print("NOTE : You can check your hunger in order/eat food.")
    time.sleep(2)
    user = name()
    time.sleep(0.2)
    while meow:
        choice = decision(user)
        if choice == 1:
                bank(user)
        elif choice == 2:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                slot_machine(user)
        elif choice == 3:
            if hunger == 10 :
                print("Your hungry")
            else:
                hunger += 1
                rock_paper_siccors(user)
        elif choice == 4:
                order_food(user )
        elif choice == 5:
            if hunger == 10 :
                print("Your hungry")
                continue
            else:
                hunger += 1
                calculator(user)
        elif choice == 6:
                eat_food(user)
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
            if knowledge <= 7:
                print("Low knowledge, You need atleast 8 knowledge points to access it!")
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
                dice_roller(user )
        elif choice == 11:
                knowledge = ball_knowledge(user)
        elif choice == 12:
                stats(user)
        else:
            ask_user = input("Are you sure ?(y/n) :")
            if ask_user == "n":
                print("Phew !! , You got me there lad")
                decision(user)
            elif ask_user == "y":
                print("You Died!")
                meow = False
                stats()
            else:
                print(f"Its a serious matter {user} !")
                ask_user = input("Are you sure ?(y/n) :")

if __name__ == "__main__":
    main()