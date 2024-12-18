def is_in_bounds(x, y, x_max, y_max):
    if (0 <= x and x < x_max) and (0 <= y and y < y_max):
        return True
    else:
        return False

def change_direction(direction):
    if direction == 3:
        direction = 0
    else:
        direction += 1
    
    return direction

def move(guard, guard_map):
    guard_x = guard[0]
    guard_y = guard[1]
    direction = 0

    # while guard in the map bounds
    while is_in_bounds(guard_x, guard_y, len(guard_map), len(guard_map[0])):
        # check next spot based on direction
        match direction:
            # Moving up / N
            case 0:
                if is_in_bounds(guard_x - 1, guard_y, len(guard_map), len(guard_map[0])):
                    # If obstacle
                    if guard_map[guard_x - 1][guard_y] == '#':
                        direction = change_direction(direction)
                    else:
                        guard_map[guard_x][guard_y] = 'X'
                        guard_x = guard_x - 1
                else:
                    guard_map[guard_x][guard_y] = 'X'
                    return -1
            # Moving right / E
            case 1:
                if is_in_bounds(guard_x, guard_y + 1, len(guard_map), len(guard_map[0])):
                    # If obstacle
                    if guard_map[guard_x][guard_y + 1] == '#':
                        direction = change_direction(direction)
                    else:
                        guard_map[guard_x][guard_y] = 'X'
                        guard_y = guard_y + 1
                else:
                    guard_map[guard_x][guard_y] = 'X'
                    return -1
            # Moving down / S
            case 2:
                if is_in_bounds(guard_x + 1, guard_y, len(guard_map), len(guard_map[0])):
                    # If obstacle
                    if guard_map[guard_x + 1][guard_y] == '#':
                        direction = change_direction(direction)
                    else:
                        guard_map[guard_x][guard_y] = 'X'
                        guard_x = guard_x + 1
                else:
                    guard_map[guard_x][guard_y] = 'X'
                    return -1
            # Moving left / W
            case 3:
                if is_in_bounds(guard_x, guard_y - 1, len(guard_map), len(guard_map[0])):
                    # If obstacle
                    if guard_map[guard_x][guard_y - 1] == '#':
                        direction = change_direction(direction)
                    else:
                        guard_map[guard_x][guard_y] = 'X'
                        guard_y = guard_y - 1
                else:
                    guard_map[guard_x][guard_y] = 'X'
                    return -1
            # Return end code
            case _: return -1

def count_X(matrix):
    counter = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                counter += 1
    
    return counter


def main():
    guard_map = []
    guard = []

    with open("input.txt", "r") as file:
        x_coord = 0

        for row in file:
            line = row.strip()
            line = list(line)

            if ("^" in line):
                for i in range(len(line)):
                    if (line[i] == "^"):
                        guard = [x_coord, i]

            guard_map.append(line)

            x_coord += 1

    move(guard, guard_map)

    print(count_X(guard_map))



if __name__ == "__main__":
    main()