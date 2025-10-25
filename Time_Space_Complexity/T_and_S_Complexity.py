
"""
Docs: 
    1. https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/
    2. https://www.simplilearn.com/tutorials/data-structure-tutorial/time-and-space-complexity

"""
arr = [3,1,4,5,56]
for i in range(len(arr)): # BigOh (N)
    for j in range(i, len(arr)): # BigOh (N)
        if arr[i]>arr[j]:
            arr[i], arr[j] = arr[j], arr[i]


# print(f"sorted array is: {arr}") # N^2


arr =  [10, 20, 20, 10, 10, 20, 5, 20 ]
"""
Time or space complexity:
    1. If elements are unique: Then BigOh (N) - Upper Bound
    2. No unique elements all are same: Omega (N) - [10, 10, 10, 10, 10] # Omega (N) Here N value is 1 - Lower Bound
    3. Theta Notation - Average Case representation 
"""



arr_dict = {}

for i in arr:
    if i in arr_dict:
        arr_dict[i] = arr_dict[i]+1
    else:
        arr_dict[i] = 1
print(arr_dict)





