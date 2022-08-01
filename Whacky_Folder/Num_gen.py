import random

def random_():
    number = random.randint(1,2)
    return number

hit = input("State guess between 1-2: ")

i = random_()
if int(hit) == i:
    print("Win")
    print(i)
else:
    print("Lose")
    print(i)