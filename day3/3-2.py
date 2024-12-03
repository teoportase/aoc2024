import re

def main():
    matches = []
    # Regex pattern to find uncorrupted code
    func_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    # Read input values
    with open('input.txt', 'r') as file:
        for line in file:
            row = line.rstrip()

            # Store all matches
            matches.extend(re.findall(func_pattern, row))

    # Start with instructions enabled
    instructions_enabled = True
    new_matches = []

    for i in range(len(matches)):
        if (matches[i] == "don't()"):
            instructions_enabled = False
        elif (matches[i] == "do()"):
            instructions_enabled = True
        else:
            if (instructions_enabled):
                new_matches.append(matches[i])
    
    pairs = []
    # Regex pattern to find numbers from 0 to 999
    num_pattern = r"\d{1,3}"

    for match in new_matches:
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