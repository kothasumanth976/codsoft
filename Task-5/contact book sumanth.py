def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ").strip()
    if name in contact_book:
        print(f"Contact '{name}' already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address (optional): ").strip()
    address = input("Enter address (optional): ").strip()
    contact_book[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully.")

def view_contacts(contact_book):
    if not contact_book:
        print("No contacts to display.")
        return
    print("\nContacts:")
    for name, info in contact_book.items():
        print(f"Name: {name}")
        print(f"  Phone: {info['Phone']}")
        print(f"  Email: {info['Email']}\n")

def search_contact(contact_book):
    name = input("Enter the name to search: ").strip()
    if name in contact_book:
        print(f"\nContact Found:")
        print(f"Name: {name}")
        print(f"  Phone: {contact_book[name]['Phone']}")
        print(f"  Email: {contact_book[name]['Email']}") 
        print(f"  Address: {contact_book[name] ['Address']}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contact_book):
    name = input("Enter the name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contact_book = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
        elif choice == '5':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()