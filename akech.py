import random

def get_computer_choice():
    choices = ['S', 'K', 'P']
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'S' and computer == 'K') or \
         (player == 'K' and computer == 'P') or \
         (player == 'P' and computer == 'S'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Stone Knife Paper Game!")
    player_choice = input("Enter your choice (S for Stone, K for Knife, P for Paper): ").upper()
    
    if player_choice not in ['S', 'K', 'P']:
        print("Invalid choice! Please enter S, K, or P.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
