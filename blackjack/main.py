import random
from art import logo
from cards import deck

def game_logic(user_card, dealer_cards, user_response):
    user_total = sum(user_card)
    dealer_total = sum(dealer_cards)
    
    if user_response == 'y':
        user_card.append(random.choice(deck))
        dealer_cards.append(random.choice(deck))
        if user_total > 21:
            return "Sorry but you lost!"
        elif user_total == 21:
            return "Congrats!!! You have won Black-Jack!!!"
    elif user_response == 'n':
        if user_total > dealer_total or (user_total < 21 and dealer_total > 21):
            return "Congrats!!! You have won Black-Jack!!!"
        elif user_total == dealer_total:
            return "You have a draw!"
        else:
            return "Sorry but you lost!"
    else:
        return "invalid input"

def play_game():
    dealer_cards = [random.choice(deck), random.choice(deck)]
    user_card = [random.choice(deck), random.choice(deck)]
    end_game = False

    while not end_game:
        print(logo, "Welcome to BLACK JACK!!!", "You will be dealt 2 cards to start.", user_card, "The dealer first card is", dealer_cards, sep='\n')
        user_response = input("Do you want a hit? y/n: ").lower()
        result = game_logic(user_card, dealer_cards, user_response)
        print(result)
        if result != "invalid input":
            end_game = True

play_game()
