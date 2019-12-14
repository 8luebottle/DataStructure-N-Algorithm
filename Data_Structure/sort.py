"""
[Data Structure] : Sort
Bubble Sort
Gnome Sort
"""

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
