def binary_search(lst: list, target: int):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            return mid
    return None

print(binary_search([1,2,3,4,5,6,7,89,90], 89))
# https://www.askpython.com/python/examples/binary-search-algorithm-in-python