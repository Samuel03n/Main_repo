from os import remove
from re import L, S
import random

print("test")
values = list(range(2,15))
suits = "Hearts", "Diamonds", "Clubs", "Spades"

face_cards = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.suit) + " " + str(self.value)

def generate_cards():
    cards = []
    for value in values:
        for suit in suits:
            if value in face_cards:
                card = Card(face_cards[value], suit)
            else:
                card = Card(value, suit)
            cards.append(card)
    return cards

def shuffle(cards):
    shuffled = []
    while len(cards) > 0:
        rand_index = random.randrange(0, len(cards))
        shuffled.append(cards[rand_index])
        cards.pop(rand_index)
    cards = shuffled
    return cards

def draw(cards, num, location):
    for i in range(0, num):
        poppedCards.insert(location, cards.pop())
    return poppedCards

def score(list, y):
    scoring = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in list:
        if i.value in face_cards:
            i.value = face_cards[i.value]
        print(i.value)
        e = int(i.value)
        scoring[e - 2] += 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    points = 0
    for i in scoring:
        if i == 2:
            points += 2
        if i == 3:
            points += 5
        if i == 4:
            points += 10
    if y == 1:
        if points == 2:
            print("Double")
        elif points == 4:
            print("Two Doubles")
        elif points == 5:
            print("Triple")
        elif points == 7:
            print("Full House")
        elif points == 10:
            print("Quadruples")
        else:
            print("You suck at poker")
    return(points)

def trunkate(list):
    dealerhand_ = ""
    for i in list:
        dealerhand_ += i.__str__() + ", "
    dealerhand_ = dealerhand_[0 : len(dealerhand_) - 2]
    return dealerhand_

def convert(j):
    for i in j:
        if i.value in face_cards:
            i.value = face_cards[i.value]

cont = "y"
bank = 1000
f = 1
while cont == "y":
    win_condition = 1
    while f == 1:
        print("Current bank value: " + str(bank))
        bet = input("State your wager: ")
        if int(bet) <= bank:
            break
        else:
            print("You're too broke. State lower wager")
    win_condition = 1
    error = 2
    poppedCards = []
    cards = generate_cards()
    cards = shuffle(cards)

    hand = draw(cards, 7, 0)
    print("Your starting hand is: " + trunkate(hand))
        
    switching = []
    while error == 2:
        error = 0
        switching = input("State which cards you would like to switch: ").split()
        switchCards = []
        for i in switching:
            try:
                switchCards.append(int(i))
            except:
                error = 2
                print("Invalid Input")
        for i in switchCards:
            if i in switchCards:
                cards.insert(random.randrange(0, 40), hand.pop(i - 1))
                draw(cards, 1, i - 1)
            else:
                error = 2
                print("Invalid Input")
                break

    print("Your cards are now: " + (trunkate(hand)))

    error = 2
    while error == 2:
        discard = []
        corrector = 0
        x = 0
        discard = input("Select the two cards you'd like to discard: ").split()
        if len(discard) != 2:
            print("Invalid input")
        else:
            for i in discard:
                if i == "1":
                    cards.insert(random.randrange(0,40), hand.pop(0))
                    hand.insert(0, "e")
                if i == "2":
                    cards.insert(random.randrange(0,40), hand.pop(1))
                    hand.insert(1, "e")
                if i == "3":
                    cards.insert(random.randrange(0,40), hand.pop(2))
                    hand.insert(2, "e")
                if i == "4":
                    cards.insert(random.randrange(0,40), hand.pop(3))
                    hand.insert(3, "e")
                if i == "5":
                    cards.insert(random.randrange(0,40), hand.pop(4))
                    hand.insert(4, "e")
                if i == "6":
                    cards.insert(random.randrange(0,40), hand.pop(5))
                    hand.insert(5, "e")
                if i == "7":
                    cards.insert(random.randrange(0,40), hand.pop(6))
                    hand.insert(6, "e")
                if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7':
                    if corrector == 0:
                        error = 1
                else:
                    if corrector == 0:
                        print("Invalid input")
                    error = 2
                    corrector = 1

            for i in hand:
                if i == "e":
                    hand.remove(i)
                if i == "e":
                    hand.remove(i)
    print("Your final cards are: " + trunkate(hand))

    playerpoints = score(hand, 1)

    dealerhand = draw(cards, 7, 0)
    for i in range(0,5):
        dealerhand.pop()
    print("Dealer's starting hand is: " + trunkate(dealerhand))

    scoring_ = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in dealerhand:
        if i.value in face_cards:
            i.value = face_cards[i.value]
        e = int(i.value)
        scoring_[e - 2] += 1

    saved_values = []
    count = 0
    print(trunkate(dealerhand))
    for i in scoring_:
        if i == 0 or i == 1:
            j = scoring_.index(i)
            scoring_.remove(i)
            scoring_.insert(count, "e")
        if i != "e":
            saved_values.append(count + 2)
        count += 1

    convert(cards)
    count = 0
    for i in dealerhand:
        if not i.value in saved_values:
            cards.insert(random.randrange(0, 40), dealerhand.pop(count))
            draw(cards, 1, count)
        count += 1
    
    print("Dealer's hand is now: " + trunkate(dealerhand))
    convert(dealerhand)
    e = score(dealerhand, 0)
    f = score(hand, 0)
    # if e > f:
    #     win_condition = 2
    #     print("You have lost")
    # elif e == f:
    #     win_condition = 3
    #     print("You have tied. Bets have been returned")
    # else:
    #     print("You have won!")

    # if win_condition == 2:
    #     bank = bank - int(bet)
    # elif win_condition == 1:
    #     bank = bank + int(bet)
    # bank = round(bank)
    # print("You're bank value is now " + str(bank))
    # if bank < 1:
    #     print("You are now broke. You're an idiot for gambling in the first place.")
    #     cont = "n"
    # elif bank > 1:
    #     cont = input("Would you like to continue? y=yes n=no ")

    # if bank > 1:
    #     print("You have cashed out with " + str(bank) + ". Great job wasting your time gambling fake money.")