from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Make your move, human...")

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
    elif computer == "paper":
        print("computer wins!")
elif player == "paper":
    if computer == "scissors":
        print("computer wins!")
    elif computer == "rock":
        print("you win!")
elif player == "scissors":
    if computer == "rock":
        print("computer wins!")
    elif computer == "paper":
        print("you win!")
else:
    print("Please enter a valid move!")