import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
        print()

def edit_contact():
    view_contacts()
    try:
        idx = int(input("Enter the contact number to edit: ")) - 1
        if 0 <= idx < len(contacts):
            contacts[idx]["name"] = input("New name: ")
            contacts[idx]["phone"] = input("New phone: ")
            contacts[idx]["email"] = input("New email: ")
            save_contacts(contacts)
            print("✏️ Contact updated.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_contact():
    view_contacts()
    try:
        idx = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            deleted = contacts.pop(idx)
            save_contacts(contacts)
            print(f"🗑️ Contact '{deleted['name']}' deleted.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

contacts = load_contacts()
main()
