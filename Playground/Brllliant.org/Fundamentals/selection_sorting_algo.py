def selection_sort(arr):
    for current in range(len(arr)):
        min_index = current

        # Search for the minimum element's index in the unsorted part of the array
        for i in range(current + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i

        # Swap the current element with the minimum element found
        if min_index != current:
            arr[current], arr[min_index] = arr[min_index], arr[current]

# Example usage:
my_array = [64, 34, 25, 12, 22, 11, 90, 2, 51, 18]
selection_sort(my_array)
print("Sorted array:", my_array)
