import random

def get_user_choice():
    choices = {"0": "Rock", "1": "Paper", "2": "Scissors"}
    while True:
        user_input = input("Enter your choice: 0.Rock 1.Paper 2.Scissors ")
        if user_input in choices:
            return int(user_input)
        else:
            print("Invalid choice. Please enter 0, 1, or 2.")

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You Win"
    else:
        return "You Lose"

def play_game():
    print("Welcome to the game: Rock, Paper, Scissors")
    print('''Rules for playing the game:
    > Rock beats Scissors
    > Paper beats Rock
    > Scissors beats Paper''')
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        choices = ["Rock", "Paper", "Scissors"]
        print(f"Computer Choice: {choices[computer_choice]}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (Yes/No): ").strip().lower()
        if play_again != "yes":
            print("Good Bye")
            break

play_game()
