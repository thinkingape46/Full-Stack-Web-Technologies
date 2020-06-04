# Number guss game.

# Generate a random number

from random import randint
from random import shuffle

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

# Another way of generating three digti number.

def random_gen():

    list = [str(num) for num in range(0, 10)]
    shuffle(list)

    random_num = list[0] + list[1] + list[2]
    print(random_num)

# Ask the player whether they like to play.

def like_to_play():

    choice = input("Do you like to play (yes or no)? ")

    if choice not in ["yes", "no"]:
        like_to_play()
    elif choice == "yes":
        guess_game()
    elif choice == "no":
        print("See you later!")

# A function to check if there is a match.

def match_check(a, b):
    '''
    A function to check if there is a match. Takes two number in the form of a string, (player_guess_number, random number).
    '''
    clue = []
    for num in [0, 1, 2]:
        if a[num] == b[num]:
            clue.append("Match")
    return " ".join(clue)

# A function to check whether any digit in the guess matches with random number

def close_check(a, b):
    '''  A function to check whether any digit in the guess matches with the one in random number. Takes two number in the form of a string, (player_guess_number, random number).  '''
    clue = []
    for char in a:
        if char in b:
            clue.append("Close")
    return " ".join(clue)

def guess_game():
    ''' A function that keeps asking the player for the guess until the correct number is guessed. Returns if the guess number is a Match, CLose or No match.   '''

    random_number = str(random_three_num())

    game_state = []

    while len(game_state) == 0:

        try:
            player_guess = input("Please enter your guess: ")

        except:
            print("Enter three digits please..")

        if player_guess == random_number:
            print("Great! it's the right guess")
            game_state.append("win")

        elif match_check(player_guess, random_number) != "":
            print(match_check(player_guess, random_number))
            continue

        elif close_check(player_guess, random_number) == "":
            print("Nope! Sorry")
            continue

        elif close_check(player_guess, random_number) != []:
            print(close_check(player_guess, random_number))
            continue

    like_to_play()

like_to_play()
