# Name: Quick sort
# Running Time: O(nlogn), O(n^2)
# Worst case: When the array is already sorted

def quicksort(array):
    # base case, already "sorted"
    if len(array) < 2:
        return array
    else:
        # recursive case
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        lesser_elements = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater_elements = [i for i in array[1:] if i >pivot]
        return quicksort(lesser_elements) + [pivot] + quicksort(greater_elements)

print(quicksort([10, 5, 2, 3, 1, 8, 13]))
