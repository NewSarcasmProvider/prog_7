import threading

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

def multithreaded_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    left_thread = threading.Thread(target=multithreaded_quick_sort, args=(less,))
    right_thread = threading.Thread(target=multithreaded_quick_sort, args=(greater))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    unsorted_list = [3, 6, 8, 10, 1, 2, 1]

    sorted_list = multithreaded_quick_sort(unsorted_list)
    print("Sorted List:", sorted_list)
