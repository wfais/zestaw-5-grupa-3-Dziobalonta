from email.headerregistry import MessageIDHeader

from matplotlib.figure import figaspect


try:
    from ZADANIE1.tablica import MonitorowanaTablica
except ImportError:
    from tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3

def merge_sort(array: MonitorowanaTablica, left=None, right=None):
    
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left < right:
        middle = (left + right) // 2
    
        merge_sort(array, left, middle)
        merge_sort(array, middle+1, right)
        merge(array, left, middle, right)


def merge(array: MonitorowanaTablica, left, middle, right):
    """Merges two sorted subarrays."""

    n1 = middle - left + 1
    n2 = right - middle

    L = [array[left + i] for i in range(n1)]
    R = [array[middle + 1 + j] for j in range(n2)]

    i = j = 0
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

def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    """Performs quick sort on the given array."""

    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if left < right:
        pivot = partition(array, left, right)

        quick_sort(array, left, pivot - 1)
        quick_sort(array, pivot + 1, right)


def partition(array: MonitorowanaTablica, left, right):
    """Partitions the array into two parts."""

    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[right] = array[right], array[i+1]

    return i + 1


def tim_sort(array: MonitorowanaTablica):
    min_run = 32

    # slicing and sorting small portions of the array. The size of these slices is defined by  `min_run` size.
    n = len(array) 
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            if midpoint < end:
                # Wywołanie merge z prawidłowymi indeksami
                merge(array, start, midpoint, end)

        # Each iteration should double the size of your arrays
        size *= 2

    return array



algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]