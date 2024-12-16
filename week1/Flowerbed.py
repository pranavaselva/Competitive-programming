n = int(input())
toplant = int(input())
arr = list(map(int, input().split()))
canplant = 0

for i in range(n):
    if arr[i] == 0:
        leftCheck = i==0 or arr[i-1]==0
        rightCheck = i==n-1 or arr[i+1]==0

        if leftCheck and rightCheck:
            arr[i] = 1
            canplant += 1

            if canplant >= toplant:
                break
if canplant >= toplant:
    print(True)
else:
    print(False)
