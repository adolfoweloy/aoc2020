import sys

coordinates = {
    'B': 'upper_half',
    'F': 'lower_half',
    'R': 'upper_half',
    'L': 'lower_half'
}


def find_seat(coord: str, coord_pos: int, start: int, end: int) -> int:
    direction = coord[coord_pos:coord_pos + 1]
    half = coordinates[direction]

    offset = (end - start) - 1
    if offset == 1:
        return start if half == 'lower_half' else end - 1

    middle = (start + end) // 2

    if half == 'upper_half':
        return find_seat(coord, coord_pos + 1, middle, end)
    else:
        return find_seat(coord, coord_pos + 1, start, middle)


if __name__ == '__main__':
    path = sys.argv[1]
    seats = []

    # prepare
    with open(path, 'r') as reader:
        entries = [line for line in reader.readlines()]
        for entry in entries:
            row = find_seat(entry, 0, 0, 128)  # there are 128 rows
            col = find_seat(entry, 7, 0, 8)  # there are 8 cols
            seat = row * 8 + col
            seats.append(seat)

    # answer 1
    max_seat_number = max(seats)
    print(max_seat_number)

    # answer 2
    min_seat_number = min(seats)
    for seat in seats:
        if max_seat_number > seat > min_seat_number:
            if seat + 1 not in seats:
                print(seat + 1)
                break
            if seat - 1 not in seats:
                print(seat + 1)
                break

