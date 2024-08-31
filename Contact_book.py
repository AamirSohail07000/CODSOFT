import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")
root.configure(bg="#FFFFF0")

contacts = []

def add_contact():
    add_window = tk.Toplevel(root)
    add_window.title("Add Contact")
    add_window.geometry("300x300")
    
    tk.Label(add_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(add_window)
    name_entry.pack(pady=5)

    tk.Label(add_window, text="Phone:").pack(pady=5)
    phone_entry = tk.Entry(add_window)
    phone_entry.pack(pady=5)
    
    tk.Label(add_window, text="Email:").pack(pady=5)
    email_entry = tk.Entry(add_window)
    email_entry.pack(pady=5)

    tk.Label(add_window, text="Address:").pack(pady=5)
    address_entry = tk.Entry(add_window)
    address_entry.pack(pady=5)
    
    def save_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        
        if name and phone:
            contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
            add_window.destroy()
        else:
            messagebox.showerror("Error", "Name and Phone are required!")
    
    tk.Button(add_window, text="Save Contact", command=save_contact).pack(pady=20)

def view_contacts():
    if not contacts:
        messagebox.showinfo("Contacts", "No contacts available.")
        return
    
    contact_list = "\n".join([f"{i+1}. {contact['name']} - {contact['phone']}" for i, contact in enumerate(contacts)])
    messagebox.showinfo("Contact List", contact_list)

def search_contact():
    search_window = tk.Toplevel(root)
    search_window.title("Search Contact")
    search_window.geometry("300x150")
    
    tk.Label(search_window, text="Enter Name or Phone Number:").pack(pady=5)
    search_entry = tk.Entry(search_window)
    search_entry.pack(pady=10)
    
    def perform_search():
        query = search_entry.get()
        if query:
            found_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
            
            if found_contacts:
                result = "\n".join([f"{contact['name']} - {contact['phone']}" for contact in found_contacts])
                messagebox.showinfo("Search Results", result)
            else:
                messagebox.showinfo("Search Results", "No contact found.")
            search_window.destroy()
    
    tk.Button(search_window, text="Search", command=perform_search).pack(pady=20)

def update_contact():
    update_window = tk.Toplevel(root)
    update_window.title("Update Contact")
    update_window.geometry("300x150")
    
    tk.Label(update_window, text="Enter Name or Phone Number:").pack(pady=5)
    update_entry = tk.Entry(update_window)
    update_entry.pack(pady=10)
    
    def perform_update():
        query = update_entry.get()
        if query:
            for contact in contacts:
                if query.lower() in contact['name'].lower() or query in contact['phone']:
                    # Open another window to update details
                    edit_window = tk.Toplevel(root)
                    edit_window.title("Edit Contact")
                    edit_window.geometry("300x250")
                    
                    tk.Label(edit_window, text="Name:").pack(pady=5)
                    name_entry = tk.Entry(edit_window)
                    name_entry.insert(0, contact['name'])
                    name_entry.pack(pady=5)

                    tk.Label(edit_window, text="Phone:").pack(pady=5)
                    phone_entry = tk.Entry(edit_window)
                    phone_entry.insert(0, contact['phone'])
                    phone_entry.pack(pady=5)
                    
                    tk.Label(edit_window, text="Email:").pack(pady=5)
                    email_entry = tk.Entry(edit_window)
                    email_entry.insert(0, contact['email'])
                    email_entry.pack(pady=5)

                    tk.Label(edit_window, text="Address:").pack(pady=5)
                    address_entry = tk.Entry(edit_window)
                    address_entry.insert(0, contact['address'])
                    address_entry.pack(pady=5)
                    
                    def save_update():
                        contact.update({
                            "name": name_entry.get(),
                            "phone": phone_entry.get(),
                            "email": email_entry.get(),
                            "address": address_entry.get()
                        })
                        messagebox.showinfo("Success", "Contact updated successfully!")
                        edit_window.destroy()
                    
                    tk.Button(edit_window, text="Save Changes", command=save_update).pack(pady=20)
                    update_window.destroy()
                    return
            
            messagebox.showinfo("Update Results", "No contact found.")
            update_window.destroy()
    
    tk.Button(update_window, text="Update", command=perform_update).pack(pady=20)

def delete_contact():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Contact")
    delete_window.geometry("300x150")
    
    tk.Label(delete_window, text="Enter Name or Phone Number:").pack(pady=5)
    delete_entry = tk.Entry(delete_window)
    delete_entry.pack(pady=10)
    
    def perform_delete():
        query = delete_entry.get()
        if query:
            for contact in contacts:
                if query.lower() in contact['name'].lower() or query in contact['phone']:
                    contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    delete_window.destroy()
                    return
            
            messagebox.showinfo("Delete Results", "No contact found.")
            delete_window.destroy()
    
    tk.Button(delete_window, text="Delete", command=perform_delete).pack(pady=20)

# Create heading frame and label
Heading_frame = tk.Frame(root, bg="#B0C4DE")
Heading_frame.pack(pady=5, fill="both")

heading = tk.Label(
    Heading_frame,
    text="Contact book",
    font=("Arial ", "20"),
    bg="#B0C4DE",
    fg="#8B0000",
    width=60,
    anchor="center"
)
heading.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root, bg="#FFFFF0")
button_frame.pack(fill="both")

# Configure grid rows and columns
button_frame.grid_columnconfigure(0, weight=1)  # Add weight to the left empty column for centering
button_frame.grid_columnconfigure(3, weight=1)  # Add weight to the right empty column for centering

# Buttons
add_button = tk.Button(button_frame, text="Add", command=add_contact, bg="#32CD32", fg="white", width=20, anchor="center")
view_button = tk.Button(button_frame, text="View", command=view_contacts, bg="#4682B4", fg="white", width=20, anchor="center")
search_button = tk.Button(button_frame, text="Search", command=search_contact, bg="#FFA500", fg="white", width=20, anchor="center")
update_button = tk.Button(button_frame, text="Update", command=update_contact, bg="#1E90FF", fg="white", width=20, anchor="center")
delete_button = tk.Button(button_frame, text="Delete", command=delete_contact, bg="#FF4500", fg="white", width=20, anchor="center")

# Add buttons to the grid with centered alignment
add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
view_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
search_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
update_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
delete_button.grid(row=2, column=1, columnspan=2, pady=10, sticky="ew")

root.mainloop()
