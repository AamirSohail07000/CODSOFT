from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("To_Do_List")
root.geometry("500x500")
# root.resizable(False,False)


#define font
my_font = Font(
  family="Baskerville Old Face", 
  size = 35,
  weight="bold", 
)

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#create listbox
my_list = Listbox(my_frame,
  font= my_font,
  width = 35,
  height=8,
  bg="lightgray",
  bd= 0,
  fg="#464646",
  highlightthickness=0,
  selectbackground="#a6a6a6",
  activestyle="none",
  )

my_list.pack(side=LEFT, fill=BOTH)

#create dummy list
Tasks = ["Go for a walk", "Do yoga", "Bring Groceries", "Solve Leetcode Questions"]
#Add dummy list to list box
for item in Tasks:
  my_list.insert(END, item)

#Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#create entry box to add items to the list
my_entry = Entry(root, font = ("Helvetica", 24))
my_entry.pack(pady=20)

#Create a button frame
Button_frame = Frame(root)
Button_frame.pack(pady=2)

#Functions
def delete_item():
  my_list.delete(ANCHOR)

def add_item():
  my_list.insert(END, my_entry.get())
  my_entry.delete(0, END)

def cross_item():
  #Cross item
  my_list.itemconfig(
    my_list.curselection(),
    fg="#dedede"
  )
  #Remove selection bar
  my_list.select_clear(0,END)

def uncross_item():
  #Cross item
  my_list.itemconfig(
    my_list.curselection(),
    fg="#464646"
  )
  #Remove selection bar
  my_list.select_clear(0,END)


#Create buttons
delete_button = Button(Button_frame, text="Delete Item", command=delete_item)
add_button = Button(Button_frame, text="Add Item", command=add_item)
cross_button = Button(Button_frame, text="Cross Item", command=cross_item)
uncross_button = Button(Button_frame, text="Uncross Item", command=uncross_item)


#Add buttons
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=15)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=15)



root.mainloop()