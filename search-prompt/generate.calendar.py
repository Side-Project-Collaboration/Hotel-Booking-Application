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

# Create a TextCalendar object for the month of April 2023
cal = calendar.TextCalendar(calendar.MONDAY)
calendar_text = cal.formatmonth(2023, 4)

# Print the calendar
print(calendar_text)
