from tkinter import *
from PIL import ImageTk

window = Tk()

# Add widgets and set up your GUI here
frame = Frame(window)
frame.pack(side="top", pady=20)  # Center the frame vertically with padding

# Create a label widget and place it in the frame using grid geometry manager
usernameLabel = Label(frame, text="username")
usernameLabel.grid(row=0, column=0, padx=10, pady=5)  # Add padx and pady to create space

usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)

emailLabel = Label(frame, text="email")
emailLabel.grid(row=1, column=0)
emailEntry = Entry(frame, width=30)
emailEntry.grid(row=1, column=1)

passwordLabel = Label(frame, text="password")
passwordLabel.grid(row=2, column=0, padx=10, pady=5)  # Add padx and pady to create space
passwordEntry = Entry(frame, width=30)
passwordEntry.grid(row=2, column=1)

submit_button = Button(window, text="Submit")
submit_button.pack(side="bottom")  # Place the button at the bottom of the window

window.mainloop()