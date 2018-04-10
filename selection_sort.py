# Name: Selection Sort
# Running Time: O(n^2)

def find_smallest(array):
    """Finds the smallest element of an arrayay and returns its index"""
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    """Sorts an arrayay by finding its smallest or biggest element"""
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array

print(selection_sort([5, 3, 6, 2, 10]))
