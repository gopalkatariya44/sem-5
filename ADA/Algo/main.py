def selection():
    # Python program for implementation of Selection
    # Sort
    import sys
    arr = [64, 25, 12, 22, 11]

    # Traverse through all array elements
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

    # Swap the found minimum element with
    # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Driver code to test above
    print("Sorted array")
    for i in range(len(arr)):
        print("%d" % arr[i]),




if __name__ == '__main__':
    selection()
