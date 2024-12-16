import difflib
from datetime import date, datetime, timedelta


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

def get_valid_date(prompt, future_allowed=False):
    """Get and validate a date input"""
    while True:
        try:
            date_str = input(prompt)
            input_date = datetime.strptime(date_str, "%d/%m/%Y").date()

            # Check if date is not in future (for birthdate)
            if not future_allowed and input_date > date.today():
                print("⛔Error: Date cannot be in the future.")
                continue

            # Check if date is not too far in past (for birthdate)
            if not future_allowed and input_date < date.today() - timedelta(days=365 * 110):
                print("⛔Error: Date cannot be more than 110 years ago.")
                continue

            return input_date
        except ValueError:
            print("⛔Invalid date format. Please use dd/mm/yyyy format.")

