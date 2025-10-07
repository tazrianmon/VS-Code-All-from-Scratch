# Number Guessing Game (Project 2)

import random

def read_guess(prompt: str, low: int = 1, high: int = 100) -> int:
    """Read a single integer guess in [low, high]. Re-prompt on invalid input."""
    while True:
        text = input(prompt).strip()
        try:
            guess = int(text)
        except ValueError:
            print("Invalid input: please enter a whole number (e.g., 42).")
            continue

        if not (low <= guess <= high):
            print(f"Out of range: enter a number between {low} and {high}.")
            continue

        return guess

def main():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess = read_guess("Enter your guess: ")
        attempts += 1

        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            plural = "attempt" if attempts == 1 else "attempts"
            print(f"Congratulations! You've guessed the number in {attempts} {plural}.")
            break

if __name__ == "__main__":
    main()
