from common import *

with open("5/input.txt", "r") as file:
    data = file.read().split('\n')

max = 0

for line in data:
    row = get_row(line)
    column = get_column(line)
    seatid = get_seatid(row, column)

    #print(f"line={line}, row={row}, column={column}, seatid={seatid}")

    if seatid > max:
        max = seatid

print(max)
