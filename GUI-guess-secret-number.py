import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text='Guess the secret number from 1 to 20:')
greeting.pack()

secret = random.randint(1, 20)

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

# check guess

# check guess
def check_guess():
    if int(guess.get()) == secret:
        result_text = "Congratulations! It's number %s! :)" % secret
    elif int(guess.get()) > secret:
        result_text = "WRONG! Your guess is too high. :("
    else:
        result_text = "WRONG! Your guess is too low. :("

    tkMessageBox.showinfo("Result", result_text)

# submit button
submit = Tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()

window.mainloop()