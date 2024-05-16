# ======== Contact Management System ======== #
"""Project Requirements
Your task is to develop a Contact Management System with the following features:

User Interface (UI):
Create a user-friendly command-line interface (CLI) for the Contact Management System.
Display a welcoming message and provide a menu with the following options:
``` Welcome to the Contact Management System! Menu:
Add a new contact
Edit an existing contact
Delete a contact
Search for a contact
Display all contacts
Export contacts to a text file
Import contacts from a text file *BONUS
Quit "> 
"""

"""
Contact Data Storage:
Use nested dictionaries as the main data structure for storing contact information.
Each contact should have a unique identifier (e.g., a phone number or email address) as the outer 
dictionary key.
Store contact details within the inner dictionary, including:
Name
Phone number
Email address
Additional information (e.g., address, notes).

Menu Actions:
Implement the following actions in response to menu selections:
Adding a new contact with all relevant details.
Editing an existing contact's information (name, phone number, email, etc.).
Deleting a contact by searching for their unique identifier.
Searching for a contact by their unique identifier and displaying their details.
Displaying a list of all contacts with their unique identifiers."""
import re
contact_data = {}

def contact_data_storage():
    print("Lets Add a New Contact")
    while True:
        email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{3,}\b")
        good_email_address = input("Please enter a valid email address. ").lower().strip()
        email_address = re.match(email_pattern, good_email_address)
        if email_address:
            print(f"Valid email: {email_address.group()}")
            break
        else:
            print("Invalid Email Please try again")
        
    print("Please enter a first and last name. ") 
    first_name = input("What is the first name? ").lower()
    last_name =input("What is the last name? ").lower()
    while True:
        good_phone_number = input("Please enter a valid phone number") 
        phone_number = re.search(r"\d{3}-\d{3}-\d{4}", good_phone_number)
        if phone_number:
            print(f"Valid Phone Number: {phone_number.group()}")
            break
        else:
            print("Please enter a valid phone number!")
    address = input("Please enter the contact's mailing address. ").lower()
    while True:
        birthday_patter = re.compile(r"\d{2}/\d{2}/\d{4}")
        birthday = input("Please enter a birthday for the contact. ").lower()
        valid_birthday = re.match(birthday_patter, birthday) 
        if valid_birthday:
            print(f" Birthday is: {valid_birthday.group()}") 
            break
        else:
            print("Please enter valid birthday!")
    notes = input("Notes: ").lower()
    contact_data[email_address.group()] = {"Name": {first_name, last_name}, "Phone Number": {phone_number.group()}, "Address": {address}, "Birthday": {birthday}, "Notes": {notes}}
    print(contact_data)

def locate_contact():
    print("Lets Locate a contact!")
    while True:
        email_address = input("Please enter the contact's email address. ").lower()
        if email_address in contact_data:
            print(contact_data[email_address])
            return (contact_data[email_address])
           
        else:
            print("Please enter a valid email address!")
        

def update_contact():
    while True:
        email_address = locate_contact()
        update = input("""What would you like to update? 
1. Email
2. Name
3. Phone Number
4. Address
5. Birthday
6. Notes 
7. Quit                               
""").lower()
        if update == "1":
            print("Please update the email address.")
            email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{3,}\b")
            good_email_address = input("Please enter a valid email address. ").lower().strip()
            new_email_address = re.match(email_pattern, good_email_address)
            if email_address in contact_data:
                print(f"Valid email: {email_address}")
                contact_data.update[email_address.group()] = contact_data[new_email_address]  # Modify value for existing key
                print("Email Updated!")  # Confirmation message
            else:
                print("Invalid Email Please try again")
 

             
        elif update == "2":
            print("Lets update the name")
            update_first_name = input("What is your first name").lower()
            update_last_name = input("What is your last name? ").lower()
            contact_data.update({"Name" : {update_first_name, update_last_name}})
            break
        elif update == "3":
            print("Please update the phone number.")
            while True:
                good_phone_number = input("Please enter a valid phone number") 
                phone_number = re.search(r"\d{3}-\d{3}-\d{4}", good_phone_number)
                if phone_number:
                    print(f"Valid Phone Number: {phone_number.group()}")
                    break
                else:
                    print("Please enter a valid phone number!")
            contact_data.update[email_address]["Phone number"] = [phone_number]   
        elif update == "4":
            print("Lets update the address.")
            new_address = input("Please update the  address. ").lower()
            contact_data[email_address]["Address"] = [new_address]
        elif update == "5":
            while True:
                birthday_patter = re.compile(r"\d{2}/\d{2}/\d{4}")
                new_birthday = input("Please update the birthday. ").lower()
                valid_birthday = re.match(birthday_patter, new_birthday) 
                if valid_birthday:
                    print(f" Birthday is: {valid_birthday.group()}")
                    contact_data[email_address]["Birthday"] = [valid_birthday]
                    break
                else:
                    print("Please enter valid birthday!")
                
        elif update == "6":
            new_notes = input("Notes: ")
            contact_data[email_address.group()]["Notes"] = [new_notes]
        elif update == "7":
            break
        else:
            print("Please enter a valid response")

# # This is a basic version of what needs to happen, we still need to make it pull and update the called ticket!
# update_contact()
def display_all_contacts():
    print(contact_data)


def delete_contact():
    contact = input("What contact would you like to delete? ").lower()
    if contact in contact_data: 
        contact_data.pop(contact)
        
# need the locate contact to populate a usable email address
     

def export_contact():
    with open("contacts.txt", "w") as file:
        for email_address in contact_data.items():
            file.write(f"{email_address}:\n") 
        



def Contact_management_system():
    while True:
         
        option = input("""Welcome to Fred's Rubber Ducky Repair Customer 
        Contact Management System! Menu:
    1. Add a new contact
    2. Edit existing contacts
    3. Delete a contact
    4. Search contacts
    5. Display contacts
    6. Export contacts to a text file
    7. Quit               
    """)  
        if option =="1":
                contact_data_storage()
        elif option == "2":
                update_contact()
                print(contact_data)
        elif option == "3":
                delete_contact()
                print(contact_data)
        elif option == "4":
                locate_contact()
        elif option == "5":
                display_all_contacts()
        elif option == "6":
                export_contact()
                print("Contacts exported!")
        elif option == "7":
             break
        else:
             print("Please enter a valid response")
             
Contact_management_system()












"""
Exporting contacts to a text file in a structured format.
Importing contacts from a text file and adding them to the system. * BONUS
User Interaction:
Utilize input() to enable users to select menu options and provide contact details.
Implement input validation using regular expressions (regex) to ensure correct formatting of contact 
information.
Error Handling:
Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may 
arise during execution.
GitHub Repository:
Create a GitHub repository for your project.
Commit your code to the repository regularly.
Create a clean and interactive README.md file in your GitHub repository.
Include clear instructions on how to run the application and explanations of its features.
Provide examples and screenshots, if possible, to enhance user understanding.
Include a link to your GitHub repository in your project documentation.
Optional Bonus Points
Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, 
work). Each contact can belong to one or more categories.
Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by 
name, phone number, email address, or additional information.
Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on 
other criteria.
Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to 
restore data from a backup file.
Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, 
anniversaries) and store this information.
"""