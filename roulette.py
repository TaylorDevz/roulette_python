########################
## GOOGLE QUERIES used to find  the required Python syntax:
##
## 1)   python random number between 1 and 10
##      ==> https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
##
## 2)   python check if string is a real number
##      ==> https://stackoverflow.com/questions/5956240/check-if-string-is-a-real-number
##
## 3)   python check if string is a number
##      ==> https://www.w3schools.com/python/ref_string_isnumeric.asp

########################
## Roulette rules
##
## random number from 0-36
##
## 0:           loses
## Odd number:  red
## Even number: black

import random
wallet_amount = float(50)

########################
## isfloat
##
## GOOGLE: python check if string is a real number
##         ==> https://stackoverflow.com/questions/5956240/check-if-string-is-a-real-number
##
def isfloat(str):
    try: 
        float(str)
    except ValueError: 
        return False
    return True

########################
## isNumberEven
##
##
def isNumberEven(n):
    remainder = n % 2 # % returns the remainder of a division / the number after the . in a decimal
    if remainder == 0:
        return True  # all even numbers can be divided by 2 without requirung a decimal point
    return False     # remainer is not 0, so its an odd number

print(f"you have {wallet_amount}$ for betting. Good luck")

########################
## main loop
##
while True:
    input_valid = False
    ####
    #### ask for bet (number/red/black)
    ####
    bet_at = input("Faites vos jeux [1-36]”, ‘R’ouge ,’N’oir, e’x’it: ")
    ####
    #### check bet (number/red/black)
    ####
    if bet_at == "x":                           # stop the game?
        break
    elif bet_at == "R" or bet_at == "r":        # Rouge?
        input_valid = True
    elif bet_at == "N" or bet_at == "n":        # Noir?
        input_valid = True
    elif bet_at.isnumeric():                    # is string a number?
        bet_at_i = int(bet_at)
        if bet_at_i >= 1 and bet_at_i <= 36:
            input_valid = True
    
    ####
    #### wrong bet input?
    ####
    if input_valid == False:
        print("wrong bet input, please try again.")
        continue # next game loop (start at while line)

    ####
    #### ask for bet amount
    ####
    while True:
        bet_amount_str = input("How much do you wish to bet? ")
        ####
        #### check that input string is a valid decimal number
        ####
        if not isfloat(bet_amount_str):
            print("you need to enter a valid number, please try again.")
            continue # next closest loop (start at while line)
        
        bet_amount = float(bet_amount_str)  # convert string into a floating pointer number e.g.  2.50        
        if bet_amount > wallet_amount:
            print(f"You have only {wallet_amount} in your wallet, you cannot bet more than that. Please try again.")
            continue 
        if bet_amount <= 0:
            print(f"Your bet has to be higher than 0$. Please try again.")
            continue 
        break # exit the enter bet amound loop

    wallet_amount -= bet_amount # take bet amount from the wallet and put the bet place the table

    ####
    #### throw the ball
    ####
    print("Faites vos jeux")
    ball_at = random.uniform(0, 36)
    ball_at = int(ball_at)
    
    ####
    #### get color from number
    ####    even => black
    ####    odd  => red
    ####
    if ball_at == 0: 
        ball_at_color = "no color"  # 0 has no coloar
    else:
        is_even = isNumberEven(ball_at)
        if is_even == True:
            ball_at_color = "Noir"      # even => black
        else:
            ball_at_color = "Rouge"     # odd  => red

    print(f"the ball landed at number: {ball_at} color: {ball_at_color}")

    ####
    #### check win
    ####
    win_amount = 0
    if ball_at != 0:                                # 0 always loses
        if bet_at == "R" or bet_at == "r":          # Rouge?     Odd number:  red
            if is_even == False:
                win_amount = bet_amount
        elif bet_at == "N" or bet_at == "n":        # Noir?     Even number: black
            if is_even == True:
                win_amount = bet_amount
        elif bet_at == ball_at:
            win_amount = bet_amount * 35 # i.e. 36-1 so that the odds are in favor of the bank

    if win_amount == 0:
        if wallet_amount <= 0:
            print(f"You lost all you money. You need to leave the table")
            break # stop the game loop
        print(f"you lost {bet_amount}$ You have {wallet_amount}$ left for betting")
        continue
    
    wallet_amount += win_amount 
    wallet_amount += bet_amount # won: keep the bet amount 
    print(f"you won {win_amount}$!!! You have now {wallet_amount}$ for betting")

########################
## stop the game
##    
print(f"Thanks for playing! You go home with {wallet_amount}$ in your wallet.")