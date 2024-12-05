def check_cross(matrix, current_pos):
    x_pos = current_pos[0]
    y_pos = current_pos[1]

    # If there is no room to make a X-cross
    if not ((0 <= x_pos-1 and x_pos+1 < len(matrix)) and (0 <= y_pos-1 and y_pos+1 < len(matrix[x_pos]))):
        return False

    # diagonal NW - bottom right to top left
    diag_NW = True if (matrix[x_pos-1][y_pos-1] == "S" and matrix[x_pos+1][y_pos+1] == "M") else False
    # diagonal SE - top left to bottom right
    diag_SE = True if (matrix[x_pos-1][y_pos-1] == "M" and matrix[x_pos+1][y_pos+1] == "S") else False

    # diagonal NE - bottom left to top right
    diag_NE = True if (matrix[x_pos+1][y_pos-1] == "S" and matrix[x_pos-1][y_pos+1] == "M") else False
    # diagonal SW - top right to bottom left
    diag_SW = True if (matrix[x_pos+1][y_pos-1] == "M" and matrix[x_pos-1][y_pos+1] == "S") else False


    if (diag_NW or diag_SE) and (diag_NE or diag_SW):
        return True
    else:
        return False


def count_XMAS(matrix):
    counter = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if (matrix[i][j] == "A"):
                current_position = [i, j]
                if (check_cross(matrix, current_position)):
                    counter += 1

    return counter


def main():
    word_search = []

    with open("input.txt", "r") as file:
        for row in file:
            line = row.rstrip()

            word_search.append(list(line))

    result = count_XMAS(word_search)

    print(result)


if __name__ == "__main__":
    main()