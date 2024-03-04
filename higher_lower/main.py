from game_data import data
from art import logo, vs
from random import shuffle, choice

deck = data[1:]
shuffle(deck)
current_deck = []


def grab_card():
    global deck
    card = choice(deck)
    current_deck.append(card)
    deck.remove(card)
    return card

def intro():
    print(logo)
    print("Welcome to higher or lower!")
    print("I am your host Zkarzzz...")

def compare_two_celebs(level_num):
    global current_deck
    global deck
    if len(deck) == 0:
        print("You have won!")
        return True
    elif len(current_deck) == 0:
        option_a = grab_card()
    else:
        option_a = current_deck[len(current_deck) - 1]
        
    option_b = grab_card()
    print(f"You are on level {level_num}")
    print(option_a["name"])
    print(vs)
    print(option_b["name"])
    user_input= input("Which celeb has higher lowers? a or b: ")
    if user_input == "a":
        if option_a["follower_count"] > option_b["follower_count"]:
            print("You are correct!")
            return False
        else:
            print("You lose")
            return True
    elif user_input == "b":
        if option_a["follower_count"] < option_b["follower_count"]:
            print("You are correct!")
            return False
        else:
            print("You lose")
            return True

        
def game(end_game = False):
    intro()
    level_num = 1
    # This will be the code to continue the loop!
    while not end_game:
        end_game = compare_two_celebs(level_num)
        level_num += 1
    print("Thank you for playing!")
    

game()
        


