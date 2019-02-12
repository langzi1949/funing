# coding = utf-8
'''
quick sort by python
'''


def partition(arr, start, end):
    base = arr[end]
    while start < end:
        while start < end and arr[start] <= base:
            start += 1
        if start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            end -= 1
        while start < end and arr[end] >= base:
            end -= 1
        if start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1

    return end


def quicksort(arr, start, end):
    if start > end:
        return

    partition_ = partition(arr, start, end)
    quicksort(arr, start, partition_ - 1)
    quicksort(arr, partition_ + 1, end)


if __name__ == '__main__':
    arr = [3, 6, 2, 9, 8, 4]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
