import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save_contacts(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
            print("\nContacts saved successfully.")
        except IOError as e:
            print(f"\nError saving contacts: {e}")

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        
        self.contacts.append({"name": name, "phone": phone, "email": email})
        print(f"Contact '{name}' added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("\nContact book is empty.")
            return
        print("\n--- All Contacts ---")
        for i, c in enumerate(self.contacts, 1):
            print(f"{i}. {c['name']} | Phone: {c['phone']} | Email: {c['email']}")

    def search_contact(self):
        query = input("\nEnter name to search: ").lower()
        results = [c for c in self.contacts if query in c['name'].lower()]
        
        if not results:
            print("No contacts found.")
        else:
            for c in results:
                print(f"Found: {c['name']} | Phone: {c['phone']} | Email: {c['email']}")

    def update_contact(self):
        name = input("\nEnter name of contact to update: ")
        for c in self.contacts:
            if c['name'].lower() == name.lower():
                print("Leave blank to keep current value.")
                new_name = input(f"New name [{c['name']}]: ")
                new_phone = input(f"New phone [{c['phone']}]: ")
                new_email = input(f"New email [{c['email']}]: ")
                
                if new_name: c['name'] = new_name
                if new_phone: c['phone'] = new_phone
                if new_email: c['email'] = new_email
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("\nEnter name of contact to delete: ")
        for i, c in enumerate(self.contacts):
            if c['name'].lower() == name.lower():
                del self.contacts[i]
                print(f"Contact '{name}' deleted.")
                return
        print("Contact not found.")

def main():
    book = ContactBook()
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Save & Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1': book.add_contact()
        elif choice == '2': book.search_contact()
        elif choice == '3': book.update_contact()
        elif choice == '4': book.delete_contact()
        elif choice == '5': book.display_contacts()
        elif choice == '6':
            book.save_contacts()
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()