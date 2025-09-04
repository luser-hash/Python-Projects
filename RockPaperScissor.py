# Rock Paper Scissor Game CLI Version

# Rules:
# 1. Rock beats Scissors
# 2. Scissors beats Paper
# 3. Paper beats Rock

# WorkFlow:
# 1. User selects Rock, Paper, or Scissors
# 2. Computer randomly selects Rock, Paper, or Scissors
# 3. Determine winner based on rules
# 4. Display result

# Core Mechanism:
# 1. Use random module to generate computer's choice
# 2. Use dictionary to map choices to their winning counterparts
# 3. Compare user choice and computer choice to determine the winner

import random

# create a dictionary to map choices to their winning counterparts
winning_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def get_computer_choice():
    return random.choice(list(winning_rules.keys()))

def detemine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif winning_rules[user_choice] == computer_choice: # This basically checks the value of the key. If it matches the computer choice, user wins. 
        return "You Win!"
    else:
        return "Computer Wins!"
    
def play_game():
    computer_choice = get_computer_choice()
    print(f"Computer chosed")

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in winning_rules:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = detemine_winner(user_choice, computer_choice)
    print(result)

def play_again():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_again()
