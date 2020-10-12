def partition(array:list, low:int, high:int):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickSort(arr, low, high):
    print(*arr)
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        part_index = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, part_index-1)
        quickSort(arr, part_index+1, high)

# Driver code to test above
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(arr)
quickSort(arr, 0, n-1)
print(*arr)