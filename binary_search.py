import random
import time

# This function performs a basic linear search through the list
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the position where the target is found
    return -1  # Return -1 if the target is not found

# This function performs a recursive binary search
def binary_search(arr, target, low=0, high=None):
    # If high isn't set, set it to the last index
    if high is None:
        high = len(arr) - 1

    # If the range is invalid, the target isn't in the list
    if low > high:
        return -1

    # Calculate the midpoint of the current range
    mid = (low + high) // 2

    # Check if the target is at the midpoint
    if arr[mid] == target:
        return mid
    # If target is less than mid value, search the left half
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    # If target is greater than mid value, search the right half
    else:
        return binary_search(arr, target, mid + 1, high)

# Main block to test both search methods
if __name__ == '__main__':
    size = 10000  # Total number of elements in the list
    data = set()

    # Fill the set with unique random integers within a large range
    while len(data) < size:
        data.add(random.randint(-3 * size, 3 * size))

    # Convert the set into a sorted list
    sorted_data = sorted(list(data))

    # Measure time taken by linear (naive) search
    start_time = time.time()
    for num in sorted_data:
        linear_search(sorted_data, num)
    print("Linear search time:", time.time() - start_time, "seconds")

    # Measure time taken by binary search
    start_time = time.time()
    for num in sorted_data:
        binary_search(sorted_data, num)
    duration = (time.time() - start_time) / size
    print("Binary search average time per lookup:", duration, "seconds")
