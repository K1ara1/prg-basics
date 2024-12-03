import json

with open('reservations.json', 'r') as file:
    content = json.load(file)
\
def print_summary(reservations):
    num_rooms = len(reservations)
    num_paid = 0
    num_unpaid = 0
    total_paid = 0
    total_unpaid = 0

    for reservation in reservations:
        if reservation["paid"] == True:
            num_paid += 1
            total_paid += reservation["value"]
        else:
            num_unpaid += 1
            total_unpaid += reservation["value"]

    print(f"Number of rooms: {num_rooms}")
    print(f"Number of paid reservations: {num_paid}")
    print(f"Number of unpaid reservations: {num_unpaid}")
    print(f"Total value of paid reservations: ${total_paid:.2f}")
    print(f"Total value of unpaid reservations: ${total_unpaid:.2f}")
        
