def solution(arr, idx):
    arr = arr[idx:]
    for i in range(len(arr)):
        if arr[i] == 1:
            return i+idx
            break
    else:
        return -1