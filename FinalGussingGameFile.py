from tkinter import *
import random

# Generate a random secret number
secret_number = random.randint(1, 10)

# Initialize attempt counter
attempt = 0

# Function to handle the guessing logic


def handle_guess(guess):
    global attempt, secret_number

    attempt += 1  # Increment the attempt counter

    if guess == secret_number:
        result_label.config(
            text=f"Congratulations! You guessed it in {attempt} attempts!"
        )
        disable_buttons()
    elif guess < secret_number:
        result_label.config(text="Too Low! Try again.")
    else:
        result_label.config(text="Too High! Try again.")

# Function to disable all buttons after winning


def disable_buttons():
    for button in buttons:
        button.config(state=DISABLED)

# Reset game


def reset_game():
    global secret_number, attempt
    secret_number = random.randint(1, 10)
    attempt = 0
    result_label.config(text="Result: None")
    number_disp_label.config(text="Selected: None")
    for button in buttons:
        button.config(state=NORMAL)


window = Tk()

window.geometry("420x420")
window.title("The Number Guessing Game")
window.config(background="#6e809c")

# Create labels
timer_label = Label(window, text="Timer:", font=(
    'Arial', 10, 'bold'), bg='#6e809c')
timer_label.place(x=0, y=0)

attempt_label = Label(window, text="Attempts:", font=(
    'Arial', 10, 'bold'), bg='#6e809c')
attempt_label.place(x=0, y=20)

# Create a label to display the countdown
time_display_lbl = Label(window, text="30 seconds",
                         font=('Arial', 10, 'bold'), bg='#6e809c')
time_display_lbl.place(x=50, y=0)

# Countdown function


def countdown(seconds=30):
    if seconds >= 0:
        time_display_lbl.config(text=f"{seconds:02d} seconds")
        window.after(1000, countdown, seconds - 1)
    else:
        time_display_lbl.config(text="Time's up!")
        disable_buttons()


# Start button
start_button = Button(window, text='Start Game', command=lambda: countdown(30))
start_button.pack()

# Label For welcoming note
welcome_label = Label(window, text='Welcome to the Guess the number Game!')
welcome_label.place(x=100, y=80)

# Label For Game Instructions
instructions_label = Label(window, text='Choose a number between 1 and 10')
instructions_label.place(x=115, y=100)

# Coordinates for button placement
start_x = 0
start_y = 130
button_width = 60
button_height = 50
button_spacing = 2

# Button labels and positions
button_labels = [
    [1, 2, 3],  # Row 1
    [4, 5, 6],  # Row 2
    [7, 8, 9],  # Row 3
    [10]        # Row 4
]

# Buttons list
buttons = []

# Place buttons using `place()`
for row_index, row in enumerate(button_labels):
    for col_index, label in enumerate(row):
        x = start_x + col_index * (button_width + button_spacing)
        y = start_y + row_index * (button_height + button_spacing)
        button = Button(
            window, text=str(label), font=('Arial', 12), width=5, height=2,
            command=lambda num=label: [number_disp_label.config(
                text=f"Selected: {num}"), handle_guess(num)]
        )
        button.place(x=x, y=y)
        buttons.append(button)

# Create a label to display the number input
number_disp_label = Label(window, text="Selected: None",
                          font=('Arial', 18), bg='#d5e2e6')
number_disp_label.place(x=220, y=220)

# Create a label to display the result
result_label = Label(window, text="Result: None",
                     font=('Arial', 12), bg='#d5e2e6')
result_label.place(x=60, y=380)

# Reset button
reset_button = Button(window, text="Reset Game",
                      font=('Arial', 12), command=reset_game)
reset_button.pack(pady=10)

window.mainloop()
