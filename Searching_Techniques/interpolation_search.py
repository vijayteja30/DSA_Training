def interpolation_search(arr, target, low, high):
    """
    [10, 12, 13, 16, 18, 19, 20, 22, 23] # Uniform way of difference

    [10,100,150, 250, 300, 350, 400, 500, 600] # Non uniform difference

    pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

    Ex:
        arr = [10, 12, 13, 16, 18, 19, 20, 22, 23]
        low, high = 0, 8
        target = 20

        pos = 0 + ((20 - 10) * (8 - 0)) // (23 - 10) = 0 + (10 * 8) // 13 = 6
        TC - O(log(log(N))) for uniform distribution
        SC - O(1)

        
        # Position won't be calculated and it directly returns -1
        target = 100
        Never calculated pos, as 100 is not in the range of arr[low] and arr[high]


        target=13
        pos = 0 + ((13 - 10) * (8 - 0)) // (23 - 10) = 0 + (3 * 8) // 13 = 1

        # Position won't be calculated and it directly returns -1
        target=250
        Never calculated pos, as 250 is not in the range of arr[low] and arr[high]


        target=23
        pos = 0 + ((23 - 10) * (8 - 0)) // (23 - 10) = 0 + (13 * 8) // 13 = 8
    """

    if low<=high and target>=arr[low] and target<=arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            return interpolation_search(arr, target, pos + 1, high)
        else:
            return interpolation_search(arr, target, low, pos - 1)
    return -1

arr = [10, 12, 13, 16, 18, 19, 20, 22, 23]
print(f"Array: {arr} and target: 20 and {interpolation_search(arr, 20, 0, len(arr) - 1)}")
print(f"Array: {arr} and target: 100 and {interpolation_search(arr, 100, 0, len(arr) - 1)}")
print(f"Array: {arr} and target: 13 and {interpolation_search(arr, 13, 0, len(arr) - 1)}")
print(f"Array: {arr} and target: 250 and {interpolation_search(arr, 250, 0, len(arr) - 1)}")
print(f"Array: {arr} and target: 11 and {interpolation_search(arr, 11, 0, len(arr) - 1)}")

