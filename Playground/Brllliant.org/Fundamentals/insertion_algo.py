def insertion_sort(arr):
    for current in range(1, len(arr)):
        key = arr[current]
        sorted_index = current - 1

        while sorted_index >= 0 and key < arr[sorted_index]:
            arr[sorted_index + 1] = arr[sorted_index]
            sorted_index -= 1

        arr[sorted_index + 1] = key

# Example usage:
my_array = [122, 111, 130, 51, 10]
insertion_sort(my_array)
print("Sorted array:", my_array)
