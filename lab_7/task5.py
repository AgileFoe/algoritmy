def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    current_max = max_element(arr, index + 1)
    return arr[index] if arr[index] > current_max else current_max