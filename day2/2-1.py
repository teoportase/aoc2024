def is_safe(array):
    # Assume levels are increasing
    increasing = True

    # Determine if levels are supposed to increase or decrease throughout report
    if (array[0] - array[1] == 0):
        return False
    elif (array[0] - array[1] > 0):
        increasing = False
    else:
        increasing = True

    # Iterate through report (except last element)
    for i in range(len(array)-1):
        difference = array[i] - array[i+1]

        # If decreasing values are found while they're supposed to be increasing
        if (increasing and difference >= 0):
            return False
        # If increasing values are found while they're supposed to be decreasing
        elif ((not increasing) and difference <= 0):
            return False

        difference = abs(difference)

        # If difference is outside acceptable boundaries
        if (1 > difference or difference > 3):
            return False
    
    return True

def main():
    safe = 0

    # Read input values and save them in 2 lists
    with open('input.txt', 'r') as file:
        for line in file:
            row = line.rstrip()
            values = row.split(" ")

            for i in range(len(values)):
                values[i] = int(values[i])

            if (is_safe(values)):
                safe += 1
                
    print(safe)

if __name__ == "__main__":
    main()