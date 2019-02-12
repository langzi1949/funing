# coding = utf-8
'''
选择排序
'''


def selectSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


if __name__ == '__main__':

    # print(selectSort([5,6,3,3,7,1]))

    print(selectSort([5, 6, 1, 4, 7, 0]))
