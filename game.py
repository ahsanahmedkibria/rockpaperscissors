
import random

# Define a function to play a round of the game and return the winner
def play_round():
    # Ask the user to choose a number (1 for rock, 2 for paper, 3 for scissors)
    user_choice = int(input("Choose 1 for rock, 2 for paper, or 3 for scissors: "))
    
    # Randomly choose a computer choice
    computer_choice = random.randint(1, 3)
    
    # Determine the winner
    if user_choice == computer_choice:
        print("Round tie!")
        return "tie"
    elif (user_choice == 1 and computer_choice == 3 or
          user_choice == 2 and computer_choice == 1 or
          user_choice == 3 and computer_choice == 2):
        print("You win this round!")
        return "user"
    else:
        print("Computer wins this round!")
        return "computer"

# Define a function to play the game until the desired number of rounds have been played
def play_game():
    num_rounds = int(input("How many rounds do you want to play? "))
    user_points = 0
    computer_points = 0
    
    for round_num in range(1, num_rounds+1):
        print(f"\nRound {round_num}:")
        winner = play_round()
        if winner == "user":
            user_points += 1
        elif winner == "computer":
            computer_points += 1
        print(f"Computer chose {random.choice(['rock', 'paper', 'scissors'])}")
        print(f"Score after round {round_num}: User {user_points} - {computer_points} Computer")
    
    # Determine the winner of the game
    if user_points == computer_points:
        print("Game tied!")
    elif user_points > computer_points:
        print("You win the game!")
    else:
        print("Computer wins the game!")

# Call the play_game function to start the game
play_game()

