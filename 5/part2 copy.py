from common import *

with open("5/input.txt", "r") as file:
    data = file.read().split('\n')

seats = []

for line in data:
    row = get_row(line)
    column = get_column(line)
    seatid = get_seatid(row, column)

    seats.append(seatid)

seats.sort()
last = seats[0] - 1

for seat in seats:
    if (seat - last > 1):
        print(seat - 1)
        break

    last = seat
