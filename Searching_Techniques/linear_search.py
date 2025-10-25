def linear_search(arr, x):
    """
        O(n) - TC
        O(1) - SC
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 50, 30, 70, 80, 20, 90, 40] #8/2 = 4
x = 300

result = linear_search(arr, x)
if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")