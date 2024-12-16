def merge(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left_part = merge(arr[:middle])
    right_part = merge(arr[middle:])

    i = j = 0
    sortedArr = []

    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            sortedArr.append(left_part[i])
            i += 1
        else:
            sortedArr.append(right_part[j])
            j += 1

    while i < len(left_part):
        sortedArr.append(left_part[i])
        i += 1

    while j < len(right_part):
        sortedArr.append(right_part[j])
        j += 1

    return sortedArr

n = int(input())
arr = list(map(int, input().split()))
ans = merge(arr)
print(*ans)