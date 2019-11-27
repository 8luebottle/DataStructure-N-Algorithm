"""
[Data Structure] : Sort
Bubble Sort
"""

# Bubble Sort
def bubble_sort(seq):
    length = len(seq)-1
    for num in range(length, 0, -1): # Sort by Descending Order
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i] # Exchange it
    return seq
