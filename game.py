import random

def guess_the_number():
    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    while not guessed_correctly:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("Too high! Try a lower number.\n")
            else:
                guessed_correctly = True
                print(f"Congratulations! 🎉 You guessed it!")
                print(f"The number was {secret_number}.")
                print(f"You took {attempts} attempts.")
                
                # Ask if they want to play again
                play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
                if play_again == "yes" or play_again == "y":
                    guess_the_number()  # Restart the game
                else:
                    print("Thanks for playing! Goodbye! 👋")
        
        except ValueError:
            print("Please enter a valid whole number.\n")

# Start the game
guess_the_number()
