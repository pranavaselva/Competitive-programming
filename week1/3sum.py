n = int(input())
arr = list(map(int, input().split()))

arr.sort()
triplets = []

for i in range(n - 2):
    if i > 0 and arr[i] == arr[i - 1]:
        continue  # Skip duplicate elements

    target_sum = 0 - arr[i]
    left, right = i + 1, n - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            triplets.append([arr[i], arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1  # Skip duplicates in the left side

            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # Skip duplicates in the right side
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

if triplets:
    for triplet in triplets:
        print(*triplet)
else:
    print("No triplet found")
