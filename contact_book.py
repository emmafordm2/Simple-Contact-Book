import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    """Load contacts from the contacts.txt file."""
    if not os.path.exists(CONTACTS_FILE):
        return {}  # Return an empty dictionary if file doesn't exist
    
    contacts = {}
    with open(CONTACTS_FILE, "r") as f:
        for line in f:
            # Each line is "Name,Phone"
            name, phone = line.strip().split(',')
            contacts[name] = phone
    return contacts

def save_contacts(contacts):
    """Save the contacts dictionary to the contacts.txt file."""
    with open(CONTACTS_FILE, "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

def display_menu():
    """Display the user menu."""
    print("\n--- Contact Book Menu ---")
    print("1. View all contacts")
    print("2. Add a new contact")
    print("3. Search for a contact")
    print("4. Exit")

def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            if not contacts:
                print("\nYour contact book is empty.")
            else:
                print("\n--- All Contacts ---")
                for name, phone in contacts.items():
                    print(f"Name: {name}, Phone: {phone}")
        
        elif choice == '2':
            name = input("Enter contact's name: ")
            phone = input("Enter contact's phone number: ")
            contacts[name] = phone
            save_contacts(contacts)
            print(f"Contact '{name}' added successfully.")

        elif choice == '3':
            search_name = input("Enter the name to search for: ")
            if search_name in contacts:
                print(f"\nFound contact: Name: {search_name}, Phone: {contacts[search_name]}")
            else:
                print(f"No contact found with the name '{search_name}'.")

        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
