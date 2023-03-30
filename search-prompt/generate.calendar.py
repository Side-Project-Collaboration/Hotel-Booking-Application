# import calendar

# def generate_calendar():
#     num_days = calendar.monthrange(2023, 4)[1]  # Get number of days in April 2023
#     calendar_header = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#     calendar = []
#     for i in range(10):  # Generate availability for 10 rooms
#         availability = [True] * num_days  # Assume all rooms are available every day
#         calendar.append(availability)
#     return [calendar_header] + calendar


# print(generate_calendar())

# print("SUPPOSE ALL ROOMS ARE AVAIABLE")

import calendar
from colorama import init, Fore, Style

# Initialize colorama
init()

# Create a TextCalendar object for the month of April 2023
cal = calendar.TextCalendar(calendar.MONDAY)

# Generate the calendar as a string
calendar_text = cal.formatmonth(2023, 4)

# Add a red marker for April 24, 2023
marker_text = f"{Fore.RED}24{Style.RESET_ALL}"
calendar_text = calendar_text.replace(' 24 ', f'{marker_text}')

# Print the modified calendar
print(calendar_text)

