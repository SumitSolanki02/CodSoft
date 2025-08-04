import random

# Options
choices = ["rock", "paper", "scissors"]

# Score counters
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors!")
print("Instructions: Type rock, paper, or scissors to play.\n")

while True:
    # User input
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please try again.\n")
        continue

    # Computer random choice
    computer_choice = random.choice(choices)

    # Show choices
    print(f"🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a tie!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("✅ You win this round!\n")
        user_score += 1
    else:
        print("❌ You lose this round!\n")
        computer_score += 1

    # Show scores
    print(f"🏆 Score -> You: {user_score} | Computer: {computer_score}")

    # Play again?
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\n👋 Thanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break

    print("-" * 40)
