class QuickSort:
    def partition(self, array, low, high):
        pivot = array[low]
        i = low + 1
        j = high

        while True:
            while i <= j and array[j] >= pivot:
                j -= 1
            while i <= j and array[i] <= pivot:
                i += 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
            else:
                break
        array[low], array[j] = array[j], array[low]
        return j

    def sort(self, array, low, high):
        if low >= high:
            return
        p = self.partition(array, low, high)
        self.sort(array, low, p-1)
        self.sort(array, p+1, high)

if __name__ == "__main__":
    array = [6, 4, 42, 32, 1, 7, 13, 12, 3, 44, 2, 6, 78, 54]
    quick = QuickSort()
    quick.sort(array, 0, len(array) - 1)
    print(array)
