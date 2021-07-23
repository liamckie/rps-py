import random
import sys

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"\nPlayer Score: {player_wins} \tComputer Score: {computer_wins}")

    player = input("\nEnter your choice : ").lower()
    if player == "quit" or player == "q":
        print("\nThank you for playing!")
        sys.exit()
    random_num = random.randint(0, 2)
    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" or player == "r":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper" or player == "p":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors" or player == "s":
        if computer == "rock":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

print(f"\nPlayer Score: {player_wins} \tComputer Score: {computer_wins}")

if player_wins > computer_wins:
    print("Congrats, You Won!")
elif player_wins == computer_wins:
    print("\nIt's a Tie")
else:
    print("\nThe Computer has Won!")
