def quicksort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    leftArr = []
    rightArr = []

    for e in arr:
        if pivot <= e:
            rightArr.append(e)
        else:
            leftArr.append(e)

    return quicksort(leftArr) + [pivot] + quicksort(rightArr[1:])


print(quicksort([3, 2, 1]))
