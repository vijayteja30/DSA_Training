def binary_search(arr, target):
    """
        TC - log(N)
        SC - O(1)
    """
    low, high = 0, len(arr)-1

    while low<=high:
        mid = (low+high)//2

        if arr[mid] ==target:
            return mid
        elif target>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    # x = 100
    # x=10
    # x=0
    # x=40
    x=3
    
    result = binary_search(arr, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
