import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    play_again = True
    
    print("Welcome to Rock, Paper, Scissors!")

    while play_again:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        print(f"\nYour score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
