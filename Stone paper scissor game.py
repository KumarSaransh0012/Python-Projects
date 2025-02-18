import random

def get_random_choice():
    # Returns a random choice from the available options
    return random.choice(('gemstone', 'paper', 'scissors'))

def prompt_user_choice():
    # Prompts the user to enter their choice and validates the input
    while True:
        user_input = input("Please enter your choice (gemstone, paper, or scissors): ").strip().lower()
        if user_input in ('gemstone', 'paper', 'scissors'):
            return user_input
        print("Invalid input. Try again.")

def evaluate_winner(player, computer):
    # Evaluates the winner based on player and computer choices
    if player == computer:
        return "It's a tie!"
    elif (
        (player == 'gemstone' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'gemstone')
    ):
        return "You're the champion!"
    return "Better luck next time!"

def main():
    print("Welcome to Gemstone, Paper, Scissors!")
    
    # Get choices
    player_choice = prompt_user_choice()
    computer_choice = get_random_choice()
    
    # Display choices
    print(f"You chose: {player_choice}")
    print(f"The computer chose: {computer_choice}")
    
    # Determine and display the winner
    result = evaluate_winner(player_choice, computer_choice)
    print(result)

if _name_ == "_main_":
    main()