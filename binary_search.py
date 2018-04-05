# Name: Binary Search
# Running Time: O(logn)

def binary_search(list, item):
    """Searchs for an item in a list, cuting by half each iteration and returns
    the position if found"""
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        # Guess was too high
        if guess > item:
            high = mid - 1
        # Guess was to low
        else:
            low = mid + 1

    # Item doesn't exists
    return None

my_list = [1, 3, 5, 7, 9]

print (binary_search(my_list, 13)) # => None
print (binary_search(my_list, 3)) # => 1
