cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    rows = len(seats) 
    cols = len(seats[0])  
    return rows * cols 

def seats_available(seats):
    available = 0
    for row in seats: 
        for seat in row: 
            if seat == 'A': 
                available += 1
    return available

def seats_booked(seats):
    booked = 0
    for row in seats: 
        for seat in row:  
            if seat == 'B': 
                booked += 1
    return booked

def seat_status(seats, row, place):
    row_index = row - 1
    place_index = place - 1

    if 0 <= row_index < len(seats) and 0 <= place_index < len(seats[0]):
        if seats[row_index][place_index] == 'A':
            return 'Available'
        else:
            return 'Booked'
    else:
        return 'Invalid seat location'

print('CINEMA INFORMATION TABLE')
print('-------------------------')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))