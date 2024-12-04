import os
import datetime
import getpass

def create_welcome_banner():
    # Get current username and time
    username = getpass.getuser()
    current_time = datetime.datetime.now()
    time_str = current_time.strftime('%I:%M %p')  # 12-hour format with AM/PM
    date_str = current_time.strftime('%B %d, %Y')  # Month Day, Year

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
