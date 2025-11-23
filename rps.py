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import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    user_action = input("Enter throw (rock, paper, scissors): ").strip().lower()
    ai_action = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

    if user_action == ai_action:
        print(f"Both players selected {user_action}. It's a tie!")

    elif user_action == "rock":
        if ai_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")

    elif user_action == "paper":
        if ai_action == "rock":
            print("Paper covers rock! You win!")
        elif ai_action == "scissors":
            print("Scissors cuts paper! You lose.")
        else:
            print("Both players selected paper. It's a tie!")

    elif user_action == "scissors":
        if ai_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    else:
        print("Invalid input. Please type rock, paper, or scissors.")

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thanks for playing!")
        break