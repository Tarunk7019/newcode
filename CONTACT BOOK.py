import tkinter as tk
from tkinter import messagebox, ttk
import os


class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        """ Load contacts from a file (if exists) """
        if os.path.exists("contacts.txt"):
            with open("contacts.txt", "r") as file:
                for line in file:
                    name, phone, email = line.strip().split(",")
                    self.contacts[name] = {"phone": phone, "email": email}

    def save_contacts(self):
        """ Save contacts to a file """
        with open("contacts.txt", "w") as file:
            for name, info in self.contacts.items():
                file.write(f"{name},{info['phone']},{info['email']}\n")

    def add_contact(self, name, phone, email):
        """ Add a new contact """
        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()
            messagebox.showinfo("Success", f"Contact {name} added.")

    def search_contact(self, name):
        """ Search for a contact by name """
        return self.contacts.get(name)

    def update_contact(self, name, new_name, new_phone, new_email):
        """ Update an existing contact """
        if name in self.contacts:
            self.contacts[new_name] = {"phone": new_phone, "email": new_email}
            if new_name != name:
                del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success", f"Contact {name} updated.")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self, name):
        """ Delete a contact by name """
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success", f"Contact {name} deleted.")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def get_contacts(self):
        """ Get all contacts """
        return self.contacts


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")  # Set background color of the root window

        self.contact_book = ContactBook()

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Contact Book", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white")
        self.title_label.pack(fill="x", pady=10)

        # Labels and entry fields with background color
        self.name_label = tk.Label(self.root, text="Name:", font=("Arial", 12), bg="#f0f0f0", anchor="w")
        self.name_label.pack(fill="x", padx=20, pady=5)

        self.name_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:", font=("Arial", 12), bg="#f0f0f0", anchor="w")
        self.phone_label.pack(fill="x", padx=20, pady=5)

        self.phone_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(self.root, text="Email:", font=("Arial", 12), bg="#f0f0f0", anchor="w")
        self.email_label.pack(fill="x", padx=20, pady=5)

        self.email_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.email_entry.pack(pady=5)

        # Buttons with background colors
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", bd=3)
        self.add_button.pack(pady=10, fill="x", padx=20)

        self.view_button = tk.Button(self.root, text="View All Contacts", command=self.view_contacts, font=("Arial", 12), bg="#2196F3", fg="white", relief="raised", bd=3)
        self.view_button.pack(pady=10, fill="x", padx=20)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact, font=("Arial", 12), bg="#FFC107", fg="white", relief="raised", bd=3)
        self.search_button.pack(pady=10, fill="x", padx=20)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact, font=("Arial", 12), bg="#FF9800", fg="white", relief="raised", bd=3)
        self.update_button.pack(pady=10, fill="x", padx=20)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, font=("Arial", 12), bg="#F44336", fg="white", relief="raised", bd=3)
        self.delete_button.pack(pady=10, fill="x", padx=20)

        # Treeview for displaying contact list with a light background
        self.contact_tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email"), show="headings")
        self.contact_tree.heading("Name", text="Name")
        self.contact_tree.heading("Phone", text="Phone")
        self.contact_tree.heading("Email", text="Email")
        self.contact_tree.pack(pady=10, padx=20)

        # Bind selection event to populate fields
        self.contact_tree.bind("<ButtonRelease-1>", self.select_item)

    def add_contact(self):
        """ Add a new contact """
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.contact_book.add_contact(name, phone, email)
            self.refresh_contacts()
        else:
            messagebox.showerror("Input Error", "Please provide name, phone, and email.")

    def view_contacts(self):
        """ View all contacts """
        self.refresh_contacts()

    def refresh_contacts(self):
        """ Refresh the contact list displayed in Treeview """
        for item in self.contact_tree.get_children():
            self.contact_tree.delete(item)
        
        contacts = self.contact_book.get_contacts()
        for name, info in contacts.items():
            self.contact_tree.insert("", "end", values=(name, info['phone'], info['email']))

    def select_item(self, event):
        """ Select an item from the contact list to update or delete """
        selected_item = self.contact_tree.selection()
        if selected_item:
            item = self.contact_tree.item(selected_item)
            name, phone, email = item['values']
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, phone)
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, email)

    def search_contact(self):
        """ Search for a contact by name """
        name = self.name_entry.get()
        if name:
            contact = self.contact_book.search_contact(name)
            if contact:
                messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
            else:
                messagebox.showerror("Error", "Contact not found.")
        else:
            messagebox.showerror("Input Error", "Please provide a name to search.")

    def update_contact(self):
        """ Update an existing contact """
        name = self.name_entry.get()
        new_name = self.name_entry.get()
        new_phone = self.phone_entry.get()
        new_email = self.email_entry.get()

        if name and new_name and new_phone and new_email:
            self.contact_book.update_contact(name, new_name, new_phone, new_email)
            self.refresh_contacts()
        else:
            messagebox.showerror("Input Error", "Please provide valid information to update.")

    def delete_contact(self):
        """ Delete a contact """
        name = self.name_entry.get()
        if name:
            self.contact_book.delete_contact(name)
            self.refresh_contacts()
        else:
            messagebox.showerror("Input Error", "Please provide a name to delete.")

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
