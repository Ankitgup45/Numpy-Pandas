print("Stone Paper Scissors Game")
print("Choices: stone, paper, scissors")

computer = "stone"  # fixed choice
user = input("Enter your choice: ").lower()

if user == computer:
    print("It's a tie!")
elif user == "paper" and computer == "stone":
    print("You win!")
elif user == "scissors" and computer == "paper":
    print("You win!")
elif user == "stone" and computer == "scissors":
    print("You win!")
else:
    print("Computer wins!")
