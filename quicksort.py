class QuickSort:
    def __init__(self):
        self.compare_count = 0
        self.move_count = 0

    def _compare(self, ele1, ele2):
        self.compare_count += 1
        return ele1 <= ele2
    
    def _move(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]
        self.move_count += 1

    def _sort(self, left, right, arr):
        # move pivot to the end for easy partition
        self._move((left + right) // 2, right, arr)
        pivot = arr[right]

        i = left
        j = right - 1

        # if i == j, need to compare to find the correct position for pivot
        while i <= j:
            while i <= j and self._compare(arr[i], pivot):
                i += 1

            while i <= j and self._compare(pivot, arr[j]):
                j -= 1

            if i < j:
                self._move(i, j, arr)
                i += 1
                j -= 1

        # move pivot back to the correct position
        self._move(i, right, arr)

        if left < i - 1:
            self._sort(left, i - 1, arr)
        if i + 1 < right:
            self._sort(i + 1, right, arr)

    def sort(self, arr):
        if len(arr) <= 1:
            return arr

        self._sort(0, len(arr) - 1, arr)
