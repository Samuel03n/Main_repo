

for i in switching:
        if i in range(1,8):
            cards.insert(random.randrange(0,40), hand.pop(i))
            draw(cards, 1, i-1)
        if i == "1":
            cards.insert(random.randrange(0,40), hand.pop(0))
            draw(cards, 1, 0)
        if i == "2":
            cards.insert(random.randrange(0,40), hand.pop(1))
            draw(cards, 1, 1)
        if i == "3":
            cards.insert(random.randrange(0,40), hand.pop(2))
            draw(cards, 1, 2)
        if i == "4":
            cards.insert(random.randrange(0,40), hand.pop(3))
            draw(cards, 1, 3)
        if i == "5":
            cards.insert(random.randrange(0,40), hand.pop(4))
            draw(cards, 1, 4)
        if i == "6":
            cards.insert(random.randrange(0,40), hand.pop(5))
            draw(cards, 1, 5)
        if i == "7":
            cards.insert(random.randrange(0,40), hand.pop(6))
            draw(cards, 1, 6)
        if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7':
            if corrector == 0:
                error = 1
        else:
            if corrector == 0:
                print("Invalid input")
            error = 2
            corrector = 1