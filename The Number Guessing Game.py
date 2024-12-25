# The random module is used for creating random secret numbers for each game
import random

# A random Number between 1 and 10 is generated for each game
secret_number = random.randint(1, 10)

print("Welcome to the Guess the number Game!")
print("Think of a number between 1 and 10 ")

# Initializing a variable to zero so that the number of attempts made for each play can be calculated each time the game is played
attempt = 0

# Game Loop
while True:

    # Try block to keep track of all the valid values entered
    try:
        # This line of code prompts the user to enter an integer

        guess = int(input("Enter your guess (Integer): "))

    # Each time an attempt is made the we increment the number of attempts by one
        attempt += 1

    # This line of code checks to see if the guessed value is equal to the secretly stored value, if true its a win
        if guess == secret_number:

            # Congratulatory statement while also counting the number of attempts
            print(
                f"Congratulations! You guessed the correct number ! in {attempt} attempts")

    # If the game has been won the while loop is exited
            break

    # This line of code tells the user how close their guessed value is to the secret_number
        if guess < secret_number:
            print("Too Low! Try again.")

    # This line of code serves the same purpose as the line of code above
        else:
            print("Too high! Try again.")

    # This except block is for handling non-integer values to prevent the programme from crashing
    except ValueError:
        print("Please Enter An Integer")
