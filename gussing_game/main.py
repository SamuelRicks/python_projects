import random
hard_mode_lives = 5
easy_mode_lives = 10
random_number = random.randint(0,100)

end_game = False
def easy_game_mode():
    global end_game
    lives = easy_mode_lives
    while lives > 0 and end_game == False:
        user_response = int(input("guess a number 1-100: "))
        if user_response > random_number:
            print("Your number is too high... Try again")
            lives -= 1
        elif user_response < random_number:
            print("Your number is too low... Try again") 
            lives -= 1
        else:
            print("Your number is spot on! You have cracked the code!")
            end_game = True
    if lives == 0:
        print("You lose! Please try again.")
    

def hard_game_mode():
    global end_game
    lives = hard_mode_lives
    while lives > 0 and end_game == False:
        user_response = int(input("guess a number 1-100: "))
        if user_response > random_number:
            print("Your number is too high... Try again")
            lives -= 1
        elif user_response < random_number:
            print("Your number is too low... Try again") 
            lives -= 1
        else:
            print("Your number is spot on! You have cracked the code!")
            end_game = True
    if lives == 0:
        print("You lose! Please try again.")
    

            

while not end_game:
    print("Welcome to the guessing game!")
    print()
    print("select a game mode")
    user_response = input("Easy or Hard: ").lower()
    if user_response == 'easy':
        easy_game_mode()
    elif user_response == 'hard':
        hard_game_mode()


