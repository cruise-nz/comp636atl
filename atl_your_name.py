# ============== AOTEAROA TOURISM MANAGEMENT SYSTEM ==============
# Student Name: 
# Student ID : 
# ================================================================
 
from datetime import datetime,timedelta     # datetime module is required for working with dates

# Make the variables and function in atl_data.py available in this code (without needing 'atl_data.' prefix)
from atl_data import customers,tours,unique_id,display_formatted_row
from welcome import create_welcome_banner
from infer_command import infer


def list_all_customers():
    """
    Lists customer details.
    This is an example of how to produce basic output."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <20}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
    display_formatted_row(["ID","First Name","Family Name","Birth Date","e-mail"],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
    for customer in customers:
        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]

        display_formatted_row([id,fname,famname,birthdate,email],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    input("\nPress Enter to continue.")

def list_customers_by_tourgroup():
    """
    Lists Customer details (including birth date), grouped by tour then tour group."""
    input("\nPress Enter to continue.")

def list_tour_details():
    """
    List the tours and all locations visited."""
    input("\nPress Enter to continue.")

def add_customer_to_tourgroup():
    """
    Choose a customer, then a tour & group, add customers to tour groups only if they meet the minimum age requirement """
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_new_customer():
    """
    Add a new customer to the customer list."""
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def list_all_destinations():
    """
    List all destinations that ATL Visit and the tours that visit them
    """
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)


def disp_menu(welcome=True):
    """
    Displays the menu and current date.  No parameters required.
    """
    if welcome:
        print(create_welcome_banner())
    print(" 1 - List Customers")
    print(" 2 - List Customers By Tour Groups")
    print(" 3 - List Tours and their details")
    print(" 4 - List all Tours that visit Destinations")
    print(" 5 - Add Existing Customer to Tour Group")
    print(" 6 - Add New Customer")
    print(" X - Exit (stops the program)")


# ------------ This is the main program ------------------------

# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"
input_command = ""
show_welcome_banner = True
while input_command != "X":
    disp_menu(show_welcome_banner)
    show_welcome_banner = False
    # Display menu for the first time, and ask for response
    input_command = input("Please enter menu choice: ")
    if input_command == "1":
        list_all_customers()
    elif input_command == "2":
        list_customers_by_tourgroup()
    elif input_command == "3":
        list_tour_details()
    elif input_command == "4":
        list_all_destinations()
    elif input_command == "5":
        add_customer_to_tourgroup()
    elif input_command == "6":
        add_new_customer()
    elif input_command != "X":
        infer_command = infer(input_command)
        print(f"\n*** Invalid input command [{input_command}], did you mean[{infer_command}], the valid command are (1-6 or X)")

    print("")

print("\n=== Thank you for using the AOTEAROA TOURS MANAGEMENT SYSTEM! ===\n")

