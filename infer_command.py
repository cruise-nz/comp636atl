import difflib

def infer(user_input):
    """Infer the closest valid command based on user input."""
    valid_commands = ['1', '2', '3', '4', '5', '6', 'X']
    # the n=1 argument returns the closest match only
    closest_match = difflib.get_close_matches(user_input, valid_commands, n=1)
    return closest_match[0] if closest_match else ''
