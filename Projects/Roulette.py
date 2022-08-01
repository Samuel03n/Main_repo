import random
import time

cont = "y"
bank = 1000

def win_loss(i):
    if i != table_num:
        print("You've lost!")
        win_condition = 2
        return win_condition
    else:
        print("You've won!")

while cont != "n":
    print("Your current bank value is " + str(bank))
    win_condition = 1
    approval = 1
    h = 1
    j = 1
    k = 1
    while approval > 0:
        wager = input("State your wager: ")
        if int(wager) > bank:
            print("You're too broke, state lower amount")
        else:
            approval = 0
            while h == 1:
                guess = input("Select 1 for red/black, 2 for odd/even, 3 for high/low, 4 for columns, 5 for dozens, or 6 for number: ")
                h = 0
                if guess == "1":
                    while j == 1:
                        red_black = input("Select 1 for red or 2 for black: ")
                        if red_black == "1" or red_black == "2":
                            break
                        else:
                            print("Invalid guess")
                        
                elif guess == "2":
                    while j == 1:
                        odd_even = input("Select 1 for odd or 2 for even: ")
                        if odd_even == "1" or odd_even == "2":
                            break
                        else:
                            print("Invalid guess")

                elif guess == "3":
                    while j == 1:
                        high_low = input("Select 1 for upper half or 2 for lower half: ")
                        if high_low == "1" or high_low == "2":
                            break
                        else:
                            print("Invalid guess")

                elif guess == "4":
                    while j == 1:
                        column = input("Select column 1, 2, or 3: ")
                        if column == "1" or column == "2" or column == "3":
                            break
                        else:
                            print("Invalid guess")

                elif guess == "5":
                    while j == 1:
                        dozen = input("Select dozen 1, 2, or 3: ")
                        if dozen == "1" or dozen == "2" or dozen == "3":
                            break
                        else:
                            print("Invalid guess")

                elif guess == "6":
                    while j == 1:
                        number = input("State the number you would like to select: ")
                        if int(number) in range(0,36):
                            break
                        else:
                            print("Invalid guess")

                else:
                    print("Invalid guess. State a real prediction")
                    h = 1

    num = random.randint(0,36)
    print("The Roulette Wheel is spun...")
    time.sleep(1)
    print("*Cool sound effects*")
    time.sleep(1)
    print("The wheel has stopped at the number: " + str(num))
    time.sleep(0.5)

    if guess == "1":
        if num in range(1,10,2) or num in range(12,19,2) or num in range(19,28,2) or num in range(30,37,2):
            table_num = "1"
        elif num == 0:
            table_num = "u suck at gambling"
        else:
            table_num = "2" 
        if table_num != red_black:
            print("You've lost!")
            bank -= int(wager)
        else:
            print("You've won!")
            bank += int(wager)

    elif guess == "2":
        if num in range(1,36,2):
            table_num = "1"
        elif num == 0:
            table_num = ";lsdkafjvb"
        else:
            table_num = "2"
        if table_num != odd_even:
            print("You've lost!")
            bank -= int(wager)
        else:
            print("You've won!")
            bank += int(wager)

    elif guess == "3":
        if num in range(19,37):
            table_num = "1"
        elif num == 0:
            table_num = "this is whack"
        else:
            table_num = "2"
        if table_num != high_low:
            print("You've lost!")
            bank -= int(wager)
        else:
            print("You've won!")
            bank += int(wager)

    elif guess == "4":
        if num in range(1,36,3):
            table_num = "1"
        elif num == 0:
            table_num = "massive L"
        elif num in range(2,36, 3):
            table_num = "2"
        else:
            table_num = "3"
        if table_num != column:
            print("You've lost!")
            bank -= int(wager)
        else:
            print("You've won!")
            bank += int(wager) * 3

    elif guess == "5":
        if num in range(1,13):
            table_num = "1"
        elif num == 0:
            table_num = "i wanna die"
        elif num in range(13,25):
            table_num = "2"
        else:
            table_num = "3"
        if table_num != dozen:
            print("You've lost!")
            bank -= int(wager)
        else:
            print("You've won!")
            bank += int(wager) * 3

    else:
        if num == int(number):
            bank += int(wager) * 36
            print("You've won!")
        else:
            bank -= int(wager)
            print("You've lost!")

    if num == 0 and number != 0:
        print("Dealer always wins lol")

    print("You're bank value is now " + str(bank))

    if bank < 1:
        print("You are now broke. You're an idiot for gambling in the first place.")
        cont = "n"
    elif bank > 1:
        while k == 1:
            cont = input("Would you like to continue? y=yes n=no ")
            if cont == "y" or cont == "n":
                break
            else:
                print("Invalid answer")

if bank > 1:
    print("You have cashed out with " + str(bank) + ". Great job wasting your time gambling fake money.")
