# Pick the median pivot and return pivot index and pivot value
def get_pivot(array):
    first = array[0]
    last = array[len(array) - 1]
    middle = array[int(len(array)/2)]

    # If first is median
    if ((middle <= first and first <= last) or (last <= first and first <= middle)):
        return 0, first
    # If middle is median
    elif ((first <= middle and middle <= last) or (last <= middle and middle <= first)):
        return int(len(array)/2), middle
    # If last is median
    else:
        return len(array) - 1, last

# Quicksort using list comprehension
def quicksort(array):
    # Base case
    if (len(array) <= 1):
        return array
    else:
        # Get the pivot
        pivot_index, pivot = get_pivot(array)

        # Move pivot to first index
        array[0], array[pivot_index] = array[pivot_index], array[0]

        # Put other values either in the left or right array based on pivot
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]

        # Return the sorted array
        return quicksort(left) + [pivot] + quicksort(right)


def compare_dist(array1, array2):
    total = 0

    # The two lists have the same length
    for i in range(len(array1)):
        dist = abs(array1[i] - array2[i])

        total += dist
    
    return total


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

    # Sort the lists
    list_1 = quicksort(list_1)
    list_2 = quicksort(list_2)

    # Compare the distances in the 2 lists
    result = compare_dist(list_1, list_2)

    print(result)


if __name__ == "__main__":
    main()