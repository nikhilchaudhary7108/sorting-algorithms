def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [10, 7, 8, 9, 1, 5]
sorted_arr = bubble_sort(arr)
print(sorted_arr)