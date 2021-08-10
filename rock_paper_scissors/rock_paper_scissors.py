from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:

    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("Make your move, human... ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer plays {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("you win!")
            player_wins += 1
        elif computer == "paper":
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "scissors":
            print("computer wins!")
            computer_wins += 1
        elif computer == "rock":
            print("you win!")
            player_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("you win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

if player_wins > computer_wins:
    print("Congrats, you won!")
elif player_wins == computer_wins:
    print("It's a tie!")
elif player == "quit" or player == "q":
    print("So be it.")
else:
    print("Better luck next time, mortal.")
print(f"Final Score: Player: {player_wins} Computer: {computer_wins}")