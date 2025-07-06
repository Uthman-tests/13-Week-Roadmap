import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 10. You have 3 attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue

            attempts += 1

            if guess == number_to_guess:
                print("Congratulations! You've guessed the number!")
                return
            elif guess < number_to_guess:
                if attempts < max_attempts:
                    print("Too low! Try again.")
            else:  # guess > number_to_guess
                if attempts < max_attempts:
                    print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
