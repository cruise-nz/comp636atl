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


def validate_email(email):
    """email validation with regex"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

