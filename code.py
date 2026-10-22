import random

def play_guessing_game():
    secret_number = random.randint(1, 20)
    print("🤖 I have chosen a secret number between 1 and 20.")
    print("You have 5 attempts to guess it. Let's begin!")
    print("-" * 40)
    
    for attempt in range(1, 6):
        # Prompt user directly via terminal input
        try:
            guess = int(input(f"Attempt {attempt}/5 | Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")
            continue
            
        # Check the guess
        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print(f"🎉 Awesome! You guessed it in {attempt} attempts!")
            return
            
        print("-" * 40)
            
    print(f"💀 Game over! The secret number was {secret_number}.")

# Start the game
play_guessing_game()