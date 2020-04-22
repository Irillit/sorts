def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = array[left: left + n1]
    R = array[mid + 1: mid + 1 + n2]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (right + left - 1) // 2
        mergeSort(array, left, mid)
        mergeSort(array, mid+1, right)
        merge(array, left, mid, right)
        

array = [2, 45, 82, 5, 23, 42, 1, 67, 8, 6]
mergeSort(array, 0, len(array) - 1)
print(array)
