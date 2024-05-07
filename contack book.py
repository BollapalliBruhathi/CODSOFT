class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name}: {contact.phone_number}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[idx]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(keyword)
            if search_results:
                print("Search Results:")
                for idx, contact in enumerate(search_results, start=1):
                    print(f"{idx}. {contact.name}: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(new_name, phone_number, email, address)
            contact_manager.update_contact(name, new_contact)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
