word = "XMAS"


def check_direction(matrix, current_pos, direction):
    has_word = True

    x_pos = current_pos[0]
    y_pos = current_pos[1]

    for i in range(1, len(word)):
        # Direction is set based on diagram in directions.png
        match direction:
            # diagonal NW
            case 1:
                if (x_pos - 1 >= 0 and y_pos - 1 >= 0):
                    x_pos -= 1
                    y_pos -= 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False

            # vertical N
            case 2:
                if (x_pos - 1 >= 0):
                    x_pos -= 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False

            # diagonal NE
            case 3:
                if (x_pos - 1 >= 0 and y_pos + 1 < len(matrix[x_pos])):
                    x_pos -= 1
                    y_pos += 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False

            # horizontal E
            case 4:
                if (y_pos + 1 < len(matrix[x_pos])):
                    y_pos += 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False

            # diagonal SE
            case 5:
                if (x_pos + 1 < len(matrix) and y_pos + 1 < len(matrix[x_pos])):
                    x_pos += 1
                    y_pos += 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False

            # vertical S
            case 6:
                if (x_pos + 1 < len(matrix)):
                    x_pos += 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False

            # diagonal SW
            case 7:
                if (x_pos + 1 < len(matrix) and y_pos - 1 >= 0):
                    x_pos += 1
                    y_pos -= 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False

            # horizontal W
            case 8:
                if (y_pos - 1 >= 0):
                    y_pos -= 1

                    if (matrix[x_pos][y_pos] == word[i]):
                        has_word = has_word and True
                    else:
                        has_word = has_word and False
                else:
                    has_word = False
            case _:
                has_word = False

    return has_word


def count_XMAS(matrix):
    counter = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if (matrix[i][j] == word[0]):
                for direction in range(1, 9):
                    current_position = [i, j]
                    if (check_direction(matrix, current_position, direction)):
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