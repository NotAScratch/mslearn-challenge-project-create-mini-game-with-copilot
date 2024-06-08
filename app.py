import random

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print("Player chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You won!")
            player_score += 1
        else:
            print("You lost!")
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            break

    print("Game over!")
    print("Player score:", player_score)
    print("Computer score:", computer_score)

play_game()