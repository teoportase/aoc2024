def main():
    list_1 = []
    list_2 = []

    # Read input values and save them in 2 lists
    with open('input.txt', 'r') as file:
        for line in file:
            row = line.rstrip()
            values = row.split("   ")
            list_1.append(int(values[0]))
            list_2.append(int(values[1]))
    
    frequency = {}

    for item in list_1:
        frequency[item] = 0
    
    for item in list_2:
        if item in frequency:
            frequency[item] += 1

    similarity = 0

    for key in frequency:
        similarity = similarity + key*frequency.get(key)

    print(similarity)

if __name__ == "__main__":
    main()