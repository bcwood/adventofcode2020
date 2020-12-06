import math

def get_row(seat):
    low = 0
    high = 127
    row_chars = seat[0:7]

    for c in row_chars:
        diff = math.ceil((high - low) / 2)
        if c == "F":
            high -= diff
        else:
            low += diff
    
    return low

def get_column(seat):
    low = 0
    high = 7
    col_chars = seat[7:10]

    for c in col_chars:
        diff = math.ceil((high - low) / 2)
        if c == "L":
            high -= diff
        else:
            low += diff
    
    return low

def get_seatid(row, column):
    return row * 8 + column