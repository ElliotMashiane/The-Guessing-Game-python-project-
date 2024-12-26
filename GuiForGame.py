from tkinter import *

window = Tk()

window.geometry("420x420")
window.title("The Number Guessing Game")
window.config(background="#6e809c")

# Create labels
timer_label = Label(window, text="Timer:", font=(
    'Arial', 10, 'bold'), bg='#6e809c')
timer_label.place(x=0, y=0)

attempt_label = Label(window, text="Attempts :",
                      font=('Arial', 10, 'bold'), bg='#6e809c')
attempt_label.place(x=0, y=20)

# Create a label to display the countdown
time_display_lbl = Label(window, text="30 seconds", font=(
    'Arial', 10, 'bold'), bg='#6e809c')
time_display_lbl.place(x=50, y=0)

# Countdown function


def countdown(seconds=30):

    if seconds >= 0:
        # Update the label with the current time
        time_display_lbl.config(text=f"{seconds:02d} seconds")
        # Call countdown again after 1 second
        window.after(1000, countdown, seconds - 1)
    else:
        # When time is up, display "Time's up!"
        time_display_lbl.config(text="Time's up!")


# Start button
start_button = Button(window, text='Start Game', command=lambda: countdown(30))
start_button.pack()

window.mainloop()
