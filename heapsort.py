class Array:
    def __init__(self, array):
        self.storage = array
        self.length = len(arr) - 1
        self.heap_size = len(arr) - 1

    def __getitem__(self, key):
        return self.storage[key]

    def __setitem__(self, key, value):
        self.storage[key] = value

def max_heapify(arr, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left <= arr.heap_size and arr[left] > arr[i]:
        largest = left

    if right <= arr.heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        tmp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = tmp
        max_heapify(arr, largest)

def build_max_heap(arr):
    for i in range(arr.length // 2, -1, -1):
        max_heapify(arr, i)

def heapsort(to_sort):
    build_max_heap(arr)
    for i in range(arr.length, 0, -1):
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp
        arr.heap_size -= 1
        max_heapify(arr, 0)

if __name__ == "__main__":
    arr = Array([56, 6, 3, 72, 13, 7, 31, 76, 92, 15, 23])
    heapsort(arr)
    print(arr.storage)
