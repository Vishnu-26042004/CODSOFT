import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contacts = load_contacts()
    
    if name in contacts:
        print("Contact already exists!")
        return
    
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    query = input("Enter Name or Phone Number to search: ")
    contacts = load_contacts()
    
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    
    if name not in contacts:
        print("Contact not found.")
        return
    
    print("Enter new details (press Enter to keep existing values):")
    phone = input(f"New Phone [{contacts[name]['phone']}]: ") or contacts[name]['phone']
    email = input(f"New Email [{contacts[name]['email']}]: ") or contacts[name]['email']
    address = input(f"New Address [{contacts[name]['address']}]: ") or contacts[name]['address']
    
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print("Contact updated successfully.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()