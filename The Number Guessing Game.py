import random

secret_number = random.randint(1, 10)

print("Welcome to the Guess the number Game!")
print("I'm thinking of a number between 1 and 10")

attempt = 0

while True:
    guess = int(input("Enter your guess: "))
    attempt += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number ! in {
              attempt} attempts")
        break
    elif guess < secret_number:
        print("Too Low! Try again.")

    else:
        print("Too high! Try again.")
