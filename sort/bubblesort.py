# coding = utf-8
'''
bubble sort by python
'''


def bubblesort(arr):
    arr_len = len(arr)
    for i in range(0, arr_len - 1):
        for j in range(0, arr_len - i-1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


if __name__ == '__main__':
    print(bubblesort([3, 5, 1, 9, 7]))
