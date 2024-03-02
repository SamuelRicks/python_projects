import random
from art import logo
from cards import deck


dealer_cards = [random.choice(deck),random.choice(deck)]
user_card = [random.choice(deck), random.choice(deck)]
end_game = False
target_value = 21
user_total = 0
dealer_total = 0

def card_sum(cards):
    total = 0
    for position in range(len(cards)):
        total += cards[position]
    return total 

while not end_game:
    print(logo)
    print("Welcome to BLACK JACK!!!")
    print()
    print("You will be delt 2 cards to start.")
    print()
    print(user_card)
    print()
    print("The dealer first card is")
    print(dealer_cards)
    print()
    user_total = card_sum(user_card)
    dealer_total = card_sum(user_card)

    user_response = input(f"Do you want a hit? y/n: ").lower()

    if user_response == 'y':
        user_card.append(random.choice(deck))
        dealer_cards.append(random.choice(deck))
        print(user_card)
        user_total = card_sum(user_card)
        dealer_total = card_sum(dealer_cards)
        if user_total > target_value:
            print("Sorry but you lost!")
            end_game = True
        elif user_total == target_value:
            print("Congrats!!! You have won Black-Jack!!!")
            end_game = True
    elif user_response == 'n':
        user_total = card_sum(user_card)
        dealer_total = card_sum(dealer_cards)
        if user_total > dealer_total:
            print("Congrats!!! You have won Black-Jack!!!")
        elif user_total < target_value and dealer_total > target_value:
            print("Congrats!!! You have won Black-Jack!!!")
            end_game = True
        elif user_total == dealer_total:
            print("You have a draw!")
            end_game == True
        else:
            print("Sorry but you lost!")
        end_game = True
    else:
        print("invalid input")
    

