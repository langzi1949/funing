# coding = utf-8
'''
insert sort by python
'''


def insertsort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        current = arr[i]
        preindex = i - 1

        while preindex >= 0 and arr[preindex] > current:
            arr[preindex + 1] = arr[preindex]
            preindex -= 1
        arr[preindex + 1] = current
    return arr


if __name__ == '__main__':
    print(insertsort([3, 1, 7, 4, 9, 0]))
