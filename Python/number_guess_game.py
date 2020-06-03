# Number guss game.

from random import randint

def random_three_num ():
    '''
    Generates a random three digit number with no repeating number.
    '''
    random_number = randint(102, 987)

    random_num = str(random_number)

    if random_num[0] == random_num[1] or random_num[0] == random_num[2] or random_num[1] == random_num[2]:
        random_three_num()

    else:
        return random_num

def like_to_play():

    choice = input("Do you like to play (yes or no)? ")

    if choice not in ["yes", "no"]:
        like_to_play()

    elif choice == "yes":
        guess_game()

    elif choice == "no":
        print("See you later!")

def match_check(a, b):
    
    for num in [0, 1, 2]:
        if a[num] == b[num]:
            return "Match"

def close_check(a, b):

    for char in a:
        if char in b:
            return "Close"
    return "Nope"

def guess_game():

    random_number = str(random_three_num())

    while True:

        try:
            player_guess = input("Please enter your guess: ")

        except:
            print("I am not using this")

        if player_guess == random_number:
            print("Great! it's the right guess")
            break

        elif close_check(player_guess, random_number) == "Nope":
            print("Nope")
            continue

        elif match_check(player_guess, random_number) == "Match":
            print("It's a Match")
            continue   

        elif close_check(player_guess, random_number) == "Close":
            print("It's Close")
            continue  

    like_to_play()

like_to_play()
