import random
import sys

VALID_CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(VALID_CHOICES)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on game rules:
    Rock beats scissors, scissors beat paper, and paper beats rock.
    """
    if user_choice == computer_choice:
        return "tie"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    
    return "computer"

def main():
    print("========================================")
    print("   Welcome to the Rock-Paper-Scissors!  ")
    print("========================================")
    
    user_score = 0
    computer_score = 0
    
    while True:
        # Prompting for user input
        print(f"\nCurrent Score -> You: {user_score} | Computer: {computer_score}")
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower().strip()
        
        if user_input not in VALID_CHOICES:
            print("Invalid input! Please enter rock, paper, or scissors.")
            continue
            
        # Generating computer selection
        computer_choice = get_computer_choice()
        
        # Displaying selections
        print(f"\nYou chose: {user_input.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Determining and displaying results
        winner = determine_winner(user_input, computer_choice)
        
        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1
            
        print("-" * 40)
        play_again = input("Do you want to play another round? (y/n): ").lower().strip()
        if play_again != 'y':
            print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame exited. Goodbye!")
        sys.exit()