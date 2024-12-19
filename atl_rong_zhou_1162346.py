# ============== AOTEAROA TOURISM MANAGEMENT SYSTEM ==============
# Student Name: Rong Zhou
# Student ID :  1162346
# ================================================================
 
from datetime import datetime, timedelta, date  # datetime module is required for working with dates

# Make the variables and function in atl_data.py available in this code (without needing 'atl_data.' prefix)
from atl_data import customers,tours,unique_id,display_formatted_row
import getpass
import difflib


# Constants defined for the program
MAXIMAL_AGE_DAYS = 365 * 110
NZ_DATE_FORMAT = "%d/%m/%Y"
# helper function start
def infer(user_input):
    """Infer the closest valid command based on user input."""
    valid_commands = ['1', '2', '3', '4', '5', '6', 'X']
    # the n=1 argument returns the closest match only
    closest_match = difflib.get_close_matches(user_input, valid_commands, n=1)
    return closest_match[0] if closest_match else ''


def calculate_age(birthdate):
    """Calculate age from birthdate"""
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def validate_email(email):
    """email validation with regex"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def create_welcome_banner():
    # Get current username and time
    username = getpass.getuser()
    current_time = datetime.now()
    time_str = current_time.strftime('%I:%M %p')  # 12-hour format with AM/PM
    date_str = current_time.strftime('%d/%m/%Y')  # day/month/year

    # Create personalized welcome message
    welcome_msg = f'Welcome, {username}!'
    time_msg = f'Current Time: {time_str}'
    date_msg = f'Date: {date_str}'

    # Calculate padding for centering messages
    width = 60
    welcome_padding = ' ' * ((width - len(welcome_msg)) // 2)
    time_padding = ' ' * ((width - len(time_msg)) // 2)
    date_padding = ' ' * ((width - len(date_msg)) // 2)

    banner = f'''
    .----------------------------------------------------------------.
      .-\'=.              .---.              .----.            .-\'-.
   .\'  .\'\'\''._.--._____.-'     '-._____.-'       '-.____.-'.\'\'\''.  \'.
   |  /                                                           \\  |
   | |         AOTEAROA TOURS MANAGEMENT SYSTEM                   | |
   | |                                                           | |
   | |{welcome_padding}{welcome_msg}{welcome_padding}| |
   | |{time_padding}{time_msg}{time_padding}| |
   | |{date_padding}{date_msg}{date_padding}| |
   |  \\                                                           /  |
    \'._\'.____________________________________________________.\'.\'
        '----------------------------------------------------'
'''
    return banner
# helper function end


# Define the functions for the menu options
def list_all_customers(show_input=True):
    """
    Lists customer details.
    This is an example of how to produce basic output."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <20}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
    display_formatted_row(["ID","First Name","Family Name","Birth Date","Email"],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
    for customer in sorted(customers, key=lambda x: (x[2], x[1])):    # Sort customers by family name, then first name
        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime(NZ_DATE_FORMAT)
        email = customer[4]

        display_formatted_row([id,fname,famname,birthdate,email],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    if show_input:
        input("\nPress Enter to continue.")

def list_customers_by_tourgroup(show_input=True):
    """Lists Customer details grouped by tour then tour group."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <20}"

    # Sort tours by name
    for tour_name in sorted(tours.keys()):
        tour = tours[tour_name]

        # Sort tour groups by date
        for tour_date in sorted(tour["groups"].keys()):
            group = tour["groups"][tour_date]

            # Display tour group header
            print(f"\n=== {tour_name} Tour - {tour_date.strftime('%B %Y')} ===")
            display_formatted_row(["ID", "First Name", "Family Name", "Birth Date", "Email"], format_str)

            if not group:  # Empty group
                print("***  NO Customers in this tour group  ***")
                continue

            # Get and sort customers in this group
            group_customers = []
            for customer_id in group:
                customer = next(c for c in customers if c[0] == customer_id)
                group_customers.append(customer)

            # Sort by family name, then first name
            group_customers.sort(key=lambda x: (x[2], x[1]))

            # Display customers
            for customer in group_customers:
                id, fname, famname, birthdate, email = customer
                birthdate_str = birthdate.strftime(NZ_DATE_FORMAT)
                display_formatted_row([id, fname, famname, birthdate_str, email], format_str)

    if show_input:
        input("\nPress Enter to continue.")

def list_tour_details(show_input=True):
    """List the tours and all locations visited."""
    if show_input:
        print("\n=== Tour Details ===")

    for tour_name in sorted(tours.keys()):
        tour = tours[tour_name]
        print(f"\nTour: {tour_name}")

        # Show age restriction if any
        if tour["age_restriction"] > 0:
            print(f"Age Restriction: {tour['age_restriction']}+")

        # Add duration information
        print(f"Destinations: {len(tour['itinerary'])} stops")

        # Join destinations with arrows
        itinerary = " -> ".join(tour["itinerary"])
        print(f"Itinerary: {itinerary}")

    if show_input:
        input("\nPress Enter to continue.")

def add_customer_to_tourgroup():
    """Add a customer to a tour group
    call process:
    1. Display available customers
    2. Get valid customer ID - Customer ID must exist
    3. Show available tours
    4. Select tour and validate age restrictions - Tour must exist
    5. Select tour date - Date must be valid
    6. Add customer if not already in group
    """
    # Display available customers
    print("\n=== Adding customer to tour, select available customers below to start ===")
    list_all_customers(False)

    # Get customer ID
    while True:
        try:
            customer_id = int(input("\nEnter customer ID: "))
            customer = next((c for c in customers if c[0] == customer_id), None)
            if customer:
                break
            print("Invalid customer ID. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Display available tours
    print("\n=== Choose one available tours ===")
    list_tour_details(False)

    # Get tour name
    while True:
        tour_name = input("\nEnter tour name(case insensitive): ").strip()
        # Find matching tour name ignoring case
        matching_tour = next((t for t in tours.keys() if t.lower() == tour_name.lower()), None)
        if matching_tour:
            tour_name = matching_tour  # Use the correct case from the dictionary
            break
        print("Invalid tour name. Available tours:", ", ".join(sorted(tours.keys())))

    # Check age restriction
    customer_age = calculate_age(customer[3])
    if customer_age < tours[tour_name]["age_restriction"]:
        print(f"⛔Error: Customer does not meet the age requirement ({tours[tour_name]['age_restriction']}+ only) of the {tour_name} tour.")
        input("\nPress Enter to continue.")
        return

    # Display available dates
    print("\n=== Choose one available dates ===")
    available_dates = sorted(tours[tour_name]["groups"].keys())
    for i, tour_date in enumerate(available_dates, 1):
        print(f"{i}. {tour_date.strftime(NZ_DATE_FORMAT)}")

    # list available date for selection
    while True:
        try:
            date_index = int(input("Select date (enter number): ")) - 1
            if 0 <= date_index < len(available_dates):
                selected_date = available_dates[date_index]
                break
            print("Invalid selection. Please try again.")
        except ValueError:
            print("⛔Please enter a valid number.")

    # Add customer to tour group
    if customer_id not in tours[tour_name]["groups"][selected_date]:
        tours[tour_name]["groups"][selected_date].append(customer_id)
        print(f"\n✅Success! Customer[{customer_id}] added to {tour_name} tour on {selected_date.strftime(NZ_DATE_FORMAT)}")
    else:
        print(f"\nCustomer[{customer_id}] is already in this tour group.")

    input("\nPress Enter to continue.")

def add_new_customer():
    """
    Add a new customer to the customer list."""
    """Add a new customer to the customer list."""
    print("\n=== Add New Customer ===")

    while True:
        # Get first name
        while True:
            first_name = input("Enter first name: ").strip()
            if first_name:
                break
            print("First name is required.")

        # Get family name
        while True:
            family_name = input("Enter family name: ").strip()
            if family_name:
                break
            print("Family name is required.")

        # Get birthdate
        birth_date = None
        while True:
            try:
                date_str = input("Enter birth date (e.g., 12/02/1996): ")
                birth_date = datetime.strptime(date_str, NZ_DATE_FORMAT).date()

                # Check if date is not in future (for birthdate)
                if birth_date > date.today():
                    print("⛔Error: Birth date cannot be in the future.")
                    continue

                # Check if date is not too far in past (for birthdate)
                if birth_date < date.today() - timedelta(days=MAXIMAL_AGE_DAYS):
                    print("⛔Error: Birth date cannot be more than 110 years ago.")
                    continue
                
                if birth_date is None:
                    continue
                else:
                    break
            except ValueError:
                print("⛔Invalid date format. Please use dd/mm/yyyy format.")

        # Get email
        while True:
            email = input("Enter email address: ").strip()
            if validate_email(email):
                break
            print("(つ╥﹏╥)つSorry, please enter a valid email address.")

        # Create new customer
        new_id = unique_id()
        customers.append([new_id, first_name, family_name, birth_date, email])

        print(f"\n✅Customer added successfully! ID: {new_id}")

        # Ask if user wants to add another customer
        if input("\n❓Add another customer? (y/n): ").lower() != 'y':
            break

def list_all_destinations(show_input=True):
    """
    List all destinations that ATL Visit and the tours that visit them
    """
    print("\n=== ATL Destinations ===")

    # Collect all unique destinations and their tours
    destinations = {}
    for tour_name, tour in tours.items():
        for destination in tour["itinerary"]:
            if destination not in destinations:
                destinations[destination] = []
            destinations[destination].append(tour_name)

    # Display destinations and their tours
    format_str = "{: <20} {}"
    display_formatted_row(["Destination", "Visited by Tours"], format_str)
    print("-" * 50)

    for destination in sorted(destinations.keys()):
        tours_list = ", ".join(sorted(destinations[destination]))
        display_formatted_row([destination, tours_list], format_str)

    if show_input:
        input("\nPress Enter to continue.")

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
    input_command = input("Please enter menu choice: ").upper()
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
        print(f"\n*** Invalid input command [{input_command}], did you mean [{infer_command}], the valid command are (1-6 or X)")

    print("")

print("\n=== Thank you for using the AOTEAROA TOURS MANAGEMENT SYSTEM! BYE!===\n")

