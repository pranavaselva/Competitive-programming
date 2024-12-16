n = int(input())
np = int(input())  
arr = []
for i in range(n):
    get = list(map(int, input().split()))
    arr.append(get)

def counting(arr, val):
    count = 0
    for i in arr:
        if i == val:
            count += 1
    return count

store1 = []
store2 = []
flag = False
s = 0

for i in range(len(arr)):
    store1.append(arr[i][0])
    store2.append(arr[i][1])

for i in range(1, np + 1):  
    if counting(store2, i) == np - 1 and i not in store1:
        flag = True
        s = i
        break
    else:
        flag = False

if flag:
    print(s)
else:
    print("-1")