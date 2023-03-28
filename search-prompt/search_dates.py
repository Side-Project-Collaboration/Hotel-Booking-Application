# Define the available rooms and their availability dates
rooms = [
    {'name': 'Standard Room', 'available_dates': ['2022-01-01', '2022-01-02', '2022-01-03']},
    {'name': 'Deluxe Room', 'available_dates': ['2022-01-02', '2022-01-03', '2022-01-04']},
    {'name': 'Suite', 'available_dates': ['2022-01-03', '2022-01-04', '2022-01-05']}
]

# Define the counter for available rooms
room_counter = len(rooms)

# Function to search for available rooms based on the desired dates
def search_rooms(checkin_date, checkout_date):
    available_rooms = []
    for room in rooms:
        if all(date in room['available_dates'] for date in [checkin_date, checkout_date]):
            available_rooms.append(room['name'])
    return available_rooms

# Example usage
checkin_date = '2022-01-02'
checkout_date = '2022-01-04'

# Search for available rooms based on the desired dates
available_rooms = search_rooms(checkin_date, checkout_date)

if available_rooms:
    # Prompt the user to select their preferred room
    print("Available rooms from {} to {}: {}".format(checkin_date, checkout_date, available_rooms))
    selected_room = input("Please select your preferred room: ")
    
    # Update the available rooms and counter based on the user's selection
    for room in rooms:
        if room['name'] == selected_room:
            room['available_dates'] = [date for date in room['available_dates'] if date not in [checkin_date, checkout_date]]
            room_counter -= 1
    print("You have successfully booked the {} from {} to {}.".format(selected_room, checkin_date, checkout_date))
    print("Remaining available rooms: {}".format(room_counter))
else:
    print("Sorry, there are no available rooms from {} to {}.".format(checkin_date, checkout_date))
