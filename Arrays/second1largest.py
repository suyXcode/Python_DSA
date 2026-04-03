

def second_largest(arr):
    if len(arr) < 2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

# Example
arr = [10, 5, 20, 8, 20]
print(second_largest(arr))  # Output: 10
