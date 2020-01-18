"""
[Data Structure] : Sort
Selection Sort
Insertion Sort
Bubble Sort
Gnome Sort
"""

# Selection Sort
def selection_sort(seq):
    length = len(seq)
    for i in range(length-1):
        min_j = i
        for j in range(i+1, length):
            if seq[min_j] > seq[j]:
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]
    return seq


# Insertion Sort
def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def insertion_sort_rec(seq, i=None):
    if i is None:
        i = len(seq) - 1
    if i == 0:
        return i
    insertion_sort_req(seq, i-1)
    j = i
    while j > 0 and seq[j-i] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq


# Bubble Sort
def bubble_sort(seq):
    length = len(seq)-1
    for num in range(length, 0, -1): # Sort by Descending Order
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i] # Exchange it
    return seq


# Gnome Sort
def gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq


#Count Sort
def count_sort_dict(a):
    b, c = [], defaultdict(list)
    for x in a:
        c[x].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b


# Quick Sort
def quick_sort_cache(seq):
    if len(seq) < 2:
        return seq
    ipivot = len(seq)
    pivot  = seq[ipivot]

    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after  = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)
