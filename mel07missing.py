"""
Gabriela Marie S. Mendez
DATALGO Lab 07
March 18, 2020
I have neither received nor provided any help on this (lab) activity,
nor have I concealed any violation of the Honor Code.
"""
def binary_search(array, low, high):
    if (low > high):
        return high + 1
    if (low != array[low]):
        return low;
    mid = int((low + high) / 2)
    if (array[mid] == mid):
        return binary_search(array, mid + 1, high)
    return binary_search(array, low, mid)
A = [0, 1, 2, 3, 6, 10, 11, 17]
n = len(A)
print("The smallest missing element is", binary_search(A, 0, n - 1))

A = [1, 2, 3, 4, 6, 11, 17]
n = len(A)
print("The smallest missing element is", binary_search(A, 0, n - 1))

A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = len(A)
print("The smallest missing element is", binary_search(A, 0, n - 1))