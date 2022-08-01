import random
from re import S
import time

cont = "y"
dealer_hit = 1
bank = 1000
f = 1

def generate():
    num = random.randint(2, 14)
    if num <= 10:
        return num
    elif num > 10 and num < 14:
        return 10
    else:
        return 11

def add(list):
    sum = 0
    for i in list:
        sum += i
    return sum

while cont == "y":
    win_condition = 1
    while f == 1:
        print("Current bank value: " + str(bank))
        bet = input("State your wager: ")
        if int(bet) <= bank:
            break
        else:
            print("You're too broke. State lower wager")

    cards = []
    dealer = []
    for i in range(2):
        cards.append(generate())
        dealer.append(generate())
    print("Your initial cards are: " + str(cards))
    print("The dealer's cards are: [X, " + str(dealer[1]) + "]")

    action = "h"
    while action == "h":
        action = input("Hit or stay (h = hit, s = stay): ")
        if action == "h": 
            cards.append(generate())
            print("Your current cards are: " + str(cards))
            print("Your cards sum up to " + str(add(cards)))
            if add(cards) > 21:
                win_condition = 2
                print("You have busted")
                break
    if add(cards) < 22:
        print("Your final cards add up to: " + str(add(cards)))

    if win_condition == 1:
        print("Dealer's starting cards cards are: " + str(dealer))
        while dealer_hit == 1:
            time.sleep(1)
            if add(dealer) > 16:
                print("Dealer's final cards add up to " + str(add(dealer)))
                break
            else:
                dealer.append(generate())
                print("Dealer's cards : " + str(dealer))
        if add(dealer) > 21:
            print("Dealer has busted")

    if add(dealer) < 22 and win_condition == 1:
        if add(dealer) > add(cards):
            win_condition = 2
            print("You have lost")
        elif add(dealer) == add(cards):
            win_condition = 3
            print("You have tied. Bets have been returned")
        else:
            print("You have won!")

    if win_condition == 2:
        bank = bank - int(bet)
    elif win_condition == 1:
        bank = bank + int(bet) * 2/3
    bank = round(bank)
    print("You're bank value is now " + str(bank))
    if bank < 1:
        print("You are now broke. You're an idiot for gambling in the first place.")
        cont = "n"
    elif bank > 1:
        cont = input("Would you like to continue? y=yes n=no ")

if bank > 1:
    print("You have cashed out with " + str(bank) + ". Great job wasting your time gambling fake money.")
