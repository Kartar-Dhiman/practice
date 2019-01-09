
def revserse(arr: list, start: int, end: int):
    """
    Description: method to reverse the array.
    """
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1


def left_rotate_reverse(arr: list, n: int, d: int):
    """
    Description: method to left rotate the array 'd' times via reversal strategy
    """
    print("rotate array via reversal strategy: ")
    print("recieved array: ", arr)
    revserse(arr, 0, d-1)
    revserse(arr, d, n-1)
    revserse(arr, 0, n-1)
    print("array after rotation: ", arr)
    print("\n***********************************************\n")


def left_rotate(arr: list, n: int, d: int):
    """
    Description: method to left rotate the array 'd' times
    """
    print("rotate array by one by one element.")
    print("recieved array: ", arr)
    for i in range(d):
        temp = arr[0]
        j = 1
        k = n-1
        while k:
            arr[j-1] = arr[j]
            j += 1
            k -= 1
        arr[n-1] = temp
    print("array after rotation: ", arr)
    print("\n***********************************************\n")


def main():
    print("\n***********************************************\n")
    arr = [1, 2, 3, 4, 5, 6, 7]
    left_rotate(arr, len(arr), 2)

    arr = [1, 2, 3, 4, 5, 6, 7]
    left_rotate_reverse(arr, len(arr), 2)


if __name__ == '__main__':
    main()
