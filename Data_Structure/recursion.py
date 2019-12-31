# Factorial
def recursion(n):
    if n == 0:
        return 1
    else:
        return n * recursion(n-1)


# Fibonacci
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Binary Search Tree
def binary_s_recur(arr, first, last, target):
    if first > last:
        return -1
    mid = int((first+last)/2)

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_s_recur(arr, first, mid-1, target)
    else:
        return binary_s_recur(arr, mid+1, last, target)


# Tower of Hanoi
def hanoi_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        hanoi_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        hanoi_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(fp, tp):
    print(f"Moving disk from {fp} to {tp}")
