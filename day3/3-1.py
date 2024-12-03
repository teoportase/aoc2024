import re

def main():
    matches = []
    # Regex pattern to find uncorrupted code
    func_pattern = r"mul\(\d{1,3},\d{1,3}\)"

    # Read input values
    with open('input.txt', 'r') as file:
        for line in file:
            row = line.rstrip()

            # Store all matches
            matches.extend(re.findall(func_pattern, row))

    pairs = []
    # Regex pattern to find numbers from 0 to 999
    num_pattern = r"\d{1,3}"

    for match in matches:
        #  Store all numbers needed to multiply in uncorrupted functions as pairs
        pairs.append(re.findall(num_pattern, match))

    # Result
    total = 0

    for pair in pairs:
        # Add the multiplications to the total
        total = total + (int(pair[0]) * int(pair[1]))

    print(total)



if __name__ == "__main__":
    main()