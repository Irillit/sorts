def insertion_sort(array):
    j = 1
    while j != len(array):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key
        j += 1

array = [9, 1, 11, 6, 3, 7, 9, 13, 74, 3, 4]
insertion_sort(array)
print(array)
