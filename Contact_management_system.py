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
import re
contact_data = {}
# def Contact_management_system():
#     print("""Welcome to Fred's Rubber Ducky Repair Customer 
#       Contact Management System! Menu:
# 1. Add a new contact
# 2. Edit existing contacts
# 3. Delete a contact
# 4. Search contacts
# 5. Display contacts
# 6. Export contacts to a text file
# 7. Import contacts from tex file
# 8. Quit               
# """)  
# Contact_management_system()
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
        
    print("Please enter a first and last name. ") # Needs to only take alphabetic characters no numbers
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
    # Throw errors for not enough numbers, any alphabetic characters
    address = input("Please enter the contact's mailing address. ").lower()
    birthday = input("Please enter a birthday for the contact. ").lower()
    notes = input("Notes: ").lower()
    contact_data[email_address] = {"Name": [first_name, last_name], "Phone Number": {phone_number}, "Address": {address}, "Birthday": {birthday}, "Notes": {notes}}
    print(contact_data)
contact_data_storage()

# def locate_contact(contact_data[email_address]):
#     print("Lets Locate a contact!")
#     while True:
#         email_address = input("Please enter the contact's email address. ").lower()
#         if email_address in contact_data:
#             print(contact_data[email_address])
#         else:
#             print("Please enter a valid email address!")
#         break
# locate_contact(contact_data[email_address])

# def update_contact():
#     while True:
#         locate_contact(contact_data["email_address"])
#         update = input("""What would you like to update? 
#     1. Email
#     2. Name
#     3. Phone Number
#     4. Address
#     5. Birthday
#     6. Notes                                
#     """).lower()
#         if update == "1":
#             new_email_address =input("Please update the email address.").lower()
#         if update == "2":
#             new_first_name = input("Please update the first name, ").lower()
#             new_last_name = input("Please update the last name.").lower()
#         if update == "3":
#             new_phone_number = input("Please update the phone number.").lower()
#         if update == "4":
#             new_address = input("Please update the  address. ").lower()
#         if update == "5":
#             new_birthday = input("Please update the birthday. ").lower()
#         if update == "6":
#             new_notes = input("Please update the notes. ")
#         if update == "7":
#             break

# # This is a basic version of what needs to happen, we still need to make it pull and update the called ticket!
# update_contact()
# def display_all_contacts():
#     print(contact_data)
# display_all_contacts()

# def delete_contact():
#     locate_contact(contact_data) 
#     deleted_contact = contact_data.pop(email_address)
# # need the locate contact to populate a usable email address
# delete_contact()       

# def export_contact():
#     with open("contacts.txt", "w")












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