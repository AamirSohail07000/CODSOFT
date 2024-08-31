from tkinter import *
import math

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        # Replace 'x' with '*' in the current input before evaluating
        expression = scvalue.get().replace('x', '*')

        try:
            value = eval(expression)  # Evaluate the expression
        except Exception as e:
            print(e)
            value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()

    elif text == "←":  # Backspace button click
      handle_backspace()    

    elif text == "%":
        try:
            current = scvalue.get()
            percentage = float(current) / 100
            scvalue.set(str(percentage))
            screen.update()
        except ValueError:
            scvalue.set("Error")
            screen.update()

    elif text == "√":
        try:
            current = scvalue.get()
            value = math.sqrt(float(current))
            scvalue.set(str(value))
            screen.update()
        except ValueError:
            scvalue.set("Error")
            screen.update()

    else: 
        # Append the text of the button to the current input
        scvalue.set(scvalue.get() + text)
        screen.update()

def handle_backspace(event=None):
    """Function to handle backspace action."""
    current = scvalue.get()
    # Remove the last character from the input
    scvalue.set(current[:-1])
    screen.update()

root = Tk()
root.geometry("400x650")
#Define max and min size
root.minsize(380,615)
root.maxsize(500,660)
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold", bd=10, insertwidth=4, width=14, justify='right')
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# List of buttons to create
f = Frame(root, bg="light grey")
buttons = [
    '6', '7', '8', '9',
    '2', '3', '4', '5',
    '1', '0', 'x', 'c',
    '+', '-', '/', "←",
    '√', '%', ".", '='  # 'x' used for multiplication
]

row, col = 0, 0
for button in buttons:
    b = Button(f, text=button, padx=20, pady=20, font="lucida 20 bold", bg="white")
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1
    
    
f.pack()

root.mainloop()
