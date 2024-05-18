import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have", max_attempts, "attempts to guess the number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number", number_to_guess, "correctly in", attempts, "attempts.")
            return

    print("Sorry, you did not guess the number. The number was:", number_to_guess)

guess_number()

