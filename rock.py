import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (1 for rock, 2 for paper, or 3 for scissors): ").lower()
        if user_choice in ['1', '2', '3']:
            return user_choice
        else:
            print("Invalid choice! Please enter 1, 2, or 3")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == '1' and computer_choice == 'scissors') or \
         (user_choice == '2' and computer_choice == 'rock') or \
         (user_choice == '3' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

play_game()