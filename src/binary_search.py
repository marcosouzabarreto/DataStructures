def binary_search(arr, tar):
    top = len(arr) - 1
    bot = 0

    while top >= bot:
        mid = int((top + bot) / 2)
        guess = arr[mid]
        if tar < guess:
            top = mid - 1
        elif tar > guess:
            bot = mid + 1
        else:
            return True

    return False


arr = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(binary_search(arr, 12))
