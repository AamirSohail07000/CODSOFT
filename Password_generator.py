import os
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

# Function to generate a password based on the selected length and combination type
def generate_password(length, combination_type):
    # Define character sets
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "!@#$%^&*()"

    if combination_type == "alpha_num":
        list_chars = alphabet + numbers
    elif combination_type == "alpha_sym":
        list_chars = alphabet + numbers + symbols
    elif combination_type == "custom":
        # Get custom input from the entry widget
        list_chars = custom_input_entry.get()
        if not list_chars:
            mb.showerror("Invalid Input", "Please enter characters for custom input.")
            return    
    else:
        list_chars = alphabet  # Default to just alphabets if no valid combination type

    # Ensure at least one character of each required type is in the password
    if combination_type == "alpha_num":
        if length < 2:
            mb.showerror("Invalid Length", "Length must be at least 2 for this combination.")
            return

        password = [random.choice(alphabet), random.choice(numbers)]
        password += random.sample(list_chars, length - 2)
    elif combination_type == "alpha_sym":
        if length < 3:
            mb.showerror("Invalid Length", "Length must be at least 3 for this combination.")
            return

        password = [random.choice(alphabet), random.choice(numbers), random.choice(symbols)]
        password += random.sample(list_chars, length - 3)

    elif combination_type == "custom":
        if length < 8:
            mb.showerror("Invalid Length", "Length must be at least 8 for this combination.")
            return

        password = random.sample(list_chars, length)
    else:
        password = random.sample(list_chars, length)

    # Convert the list into a string
    pass_str = "".join(password)

    # Display the generated password string in the label
    pass_label.config(text=pass_str)
    # Print the password string in the command line
    print("Generated Password is:", pass_str, "\n")

# Function to handle button click and generate the password
def selection():
    length_value = length.get()
    combination_type = combo_type.get()
    if length_value != 0 and combination_type:
        generate_password(length_value, combination_type)
    else:
        mb.showerror("Invalid Selection", "Length or combination type is not defined.")

# Function to retrieve the length of the password
def get_length():
    print("Selected Length of Password:", length.get(), "characters")

# Function to reset everything in the application
def reset():
    # Set the initial value of the password's length
    length.set(0)
    # Set the initial value of the combination type
    combo_type.set(None)
    # Clear the custom input entry
    custom_input_entry.delete(0, 'end')
    # Disable the custom input entry
    custom_input_entry.config(state='disabled')
    # Set the initial value of the label
    pass_label.config(text="")

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = pass_label.cget("text")  # Get the text from the label
    if password:
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(password)  # Append the text to the clipboard
        mb.showinfo("Copied", "Password copied to clipboard!")  # Show confirmation message
    else:
        mb.showwarning("No Password", "No password to copy!")
def toggle_custom_input(entry_widget, selected_type):
    """Toggle the entry widget state based on the selected combination type."""
    if selected_type == 'custom':
        entry_widget.config(state='normal')  # Enable the entry widget
    else:
        entry_widget.config(state='disabled')  # Disable the entry widget

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    root.minsize(410, 400)
    root.config(bg="#F0F8FF")
    root.title("Random Password Generator")

    # Create frames for organizing widgets
    heading_frame = Frame(root, bg="#87CEEB")
    option_frame = Frame(root, bg="#4682B4")
    button_frame = Frame(root, bg="#F0F8FF")
    result_frame = Frame(root, bg="#F0F8FF")

    # Use the pack() method to place the frames
    heading_frame.pack(fill="both")
    option_frame.pack(pady=10, fill="both")
    button_frame.pack(pady=12, fill="both")
    result_frame.pack(pady=12, fill="both")

    # Add heading label
    heading = Label(
        heading_frame,
        text="GENERATE A RANDOM PASSWORD",
        font=("Helvetica", "17"),
        bg="#87CEEB",
        fg="#556B2F",
        anchor="center"
    )
    heading.pack(pady=10)

    # Add label for selecting password length
    length_label = Label(
        option_frame,
        text="Select Password Length:",
        font=("Helvetica", "14"),
        bg="#4682B4",
        fg="#8B008B",
        anchor="w"
    )
    length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # Set up radio buttons for password length
    length = IntVar()
    length.set(0)  # Default value

    radiobuttonOne = Radiobutton(
        option_frame,
        text='8 Characters',
        variable=length,
        value=8,
        font=("Times New Roman", "12"),
        bg="#4682B4",
        command=get_length
    )
    radiobuttonTwo = Radiobutton(
        option_frame,
        text='10 Characters',
        variable=length,
        value=10,
        font=("Times New Roman", "12"),
        bg="#4682B4",
        command=get_length
    )

    radiobuttonOne.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    radiobuttonTwo.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    # Add label for selecting password combination
    combo_label = Label(
        option_frame,
        text="Select Password Combination:",
        font=("Helvetica", "14"),
        bg="#4682B4",
        fg="#8B008B",
        anchor="w"
    )
    combo_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    # Set up radio buttons for password combination type
    combo_type = StringVar()
    combo_type.set(None)  # Default value

    alpha_num_rb = Radiobutton(
        option_frame,
        text='Alphabets & Numbers',
        variable=combo_type,
        value='alpha_num',
        font=("Times New Roman", "12"),
        bg="#4682B4"
    )
    alpha_sym_rb = Radiobutton(
        option_frame,
        text='Alphabets, Numbers & Symbols',
        variable=combo_type,
        value='alpha_sym',
        font=("Times New Roman", "12"),
        bg="#4682B4"
    )
    # Step 1: Add the third radio button for custom input
    custom_input_rb = Radiobutton(
        option_frame,
        text='Custom Input',
        variable=combo_type,
        value='custom',
        font=("Times New Roman", "12"),
        bg="#4682B4",
        command=lambda: toggle_custom_input(custom_input_entry, combo_type.get())
    )

    custom_input_rb.grid(row=6, column=0, padx=10, pady=5, sticky="w")

    # Step 2: Create an Entry widget for custom input (initially hidden)
    custom_input_entry = Entry(
        option_frame,
        font=("Times New Roman", "12"),
        width=30,
        state='disabled'  # Initially disabled until custom option is selected
    )

    custom_input_entry.grid(row=7, column=0, padx=10, pady=5, sticky="w")


    alpha_num_rb.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    alpha_sym_rb.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    # Add buttons for generating password and resetting
    get_pass = Button(
        button_frame,
        text="Generate Password",
        font=("Bahnschrift SemiBold", "12"),
        width=14,
        bg="#32CD32",
        fg="#FFFFFF",
        activebackground="#006400",
        activeforeground="#FFFFFF",
        relief=GROOVE,
        command=selection
    )
    clear_all = Button(
        button_frame,
        text="Reset",
        font=("Bahnschrift SemiBold", "12"),
        width=14,
        bg="#FF0000",
        fg="#FFFFFF",
        activebackground="#8B0000",
        activeforeground="#FFFFFF",
        relief=GROOVE,
        command=reset
    )

    get_pass.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    clear_all.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    # Add a label to display the generated password
    pass_label = Label(
        result_frame,
        text="",
        font=("Consolas", "15", "bold"),
        bg="#F0F8FF",
        fg="#000000"
    )
    pass_label.pack(pady=5)

    # Add a button to copy the password to the clipboard
    copy_button = Button(
        root,
        text="Copy to Clipboard",
        bg="#F5FFFA",
        fg="#8B0000",
        command=copy_to_clipboard
    )
    copy_button.pack(pady=5)

    # Adjust grid row and column weights to center align widgets
    option_frame.grid_rowconfigure(0, weight=0)
    option_frame.grid_rowconfigure(1, weight=1)
    option_frame.grid_rowconfigure(2, weight=1)
    option_frame.grid_rowconfigure(3, weight=0)
    option_frame.grid_rowconfigure(4, weight=1)
    option_frame.grid_rowconfigure(5, weight=1)
    option_frame.grid_columnconfigure(0, weight=1)
    
    button_frame.grid_rowconfigure(0, weight=1)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

    root.mainloop()
