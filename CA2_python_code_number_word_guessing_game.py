import random

def number_guessing_game():
    print("=== Number Guessing Game ===\n")
    
    # Get valid range
    while True:
        try:
            lower = int(input("Enter the lower limit: "))
            upper = int(input("Enter the upper limit: "))
            if lower >= upper:
                print("Error: Lower limit must be less than upper limit. Try again.\n")
            else:
                break
        except ValueError:
            print("Please enter valid integers.\n")
    
    secret_number = random.randint(lower, upper)
    total_possible = upper - lower + 1
    attempts = 0
    previous_guesses = set()  # To track all guesses made
    
    print(f"\nI've picked a number between {lower} and {upper} (inclusive).")
    print("Hint: I will remember your guesses — no repeating!\n")
    
    while True:
        try:
            guess_input = input("Guess the number (or 'q' to quit): ").strip()
            
            if guess_input.lower() == 'q':
                print(f"\nThe secret number was {secret_number}.")
                print("Better luck next time!")
                break
                
            guess = int(guess_input)
            attempts += 1
            
            # Check if guess is outside range
            if guess < lower or guess > upper:
                print(f"Warning: {guess} is OUTSIDE the range [{lower}–{upper}]!")
                print("Please stay within the limits.\n")
                attempts -= 1  # Don't count invalid range guesses
                continue
            
            # Check for repeated guess
            if guess in previous_guesses:
                print(f"You already guessed {guess}! Try a different number.")
                print(f"Your previous guesses: {sorted(previous_guesses)}\n")
                attempts -= 1  # Don't count repeated guesses
                continue
            
            # Valid new guess — add to history
            previous_guesses.add(guess)
            
            # Main game feedback
            if guess < secret_number:
                print("Too low!\n")
            elif guess > secret_number:
                print("Too high!\n")
            else:
                # WINNING MESSAGE WITH PERFORMANCE
                print("=" * 55)
                print(f"Congratulations! You guessed it: {secret_number}")
                print(f"You took {attempts} attempt(s) to guess correctly.")
                print(f"Total unique guesses made: {len(previous_guesses)}")
                
                # Smart congratulatory messages
                if attempts == 1:
                    print("WOW! First try? You're a guessing legend!")
                elif attempts <= 3:
                    print("Incredible speed! You're a pro!")
                elif attempts <= max(5, int(total_possible ** 0.5)):
                    print("Excellent! Very sharp guessing!")
                elif attempts <= total_possible // 3:
                    print("Great persistence and logic!")
                else:
                    print("You got there! Every guess brought you closer.")
                
                if len(previous_guesses) < 10:
                    print(f"\nYour guessing history: {sorted(previous_guesses)}")
                
                print("=" * 55)
                break
                
        except ValueError:
            print("Please enter a valid number or 'q' to quit.\n")
            attempts -= 1 if attempts > 0 else 0

# Word game and menu remain unchanged
def word_guessing_game():
    print("\n=== Word Guessing Game ===")
    words = ["python", "laptop", "university", "arduino", "science", "programming", "island", "books", "wallpaper", 
             "microprocessor", "coffee","nachos","basket","tacos", "music", "bewildered", "amazed", "poetry","travel","marvel", "Harry Potter"]
    secret_word = random.choice(words)
    guessed_letters = []
    turns = 10
    print(f"Guess the word! You have {turns} incorrect guesses allowed.\n")
    
    while turns > 0:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        print(f"Word: {display}")
        if "_" not in display:
            print(f"\nYou won! The word was: {secret_word}")
            break
            
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        if guess not in secret_word:
            turns -= 1
            print(f"Wrong! {turns} turn(s) left.\n")
        else:
            print("Correct!\n")
            
        if turns == 0:
            print(f"Game Over! The word was: {secret_word}")

def main_menu():
    while True:
        print("\n" + "="*38)
        print("       GUESSING GAMES MENU")
        print("="*38)
        print("1. Number Guessing Game")
        print("2. Word Guessing Game")
        print("3. Exit")
        print("="*38)
        choice = input("Choose a game (1/2/3): ")
        
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_guessing_game()
        elif choice == "3":
            print("\nThanks for playing! See you next time!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Start the program
if __name__ == "__main__":
    main_menu()