# Function to find the maximum consecutive ones
def max_consecutive_ones(binary_list):
    max_count = 0
    current_count = 0

    for num in binary_list:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Taking input from the user
binary_array = list(map(int, input().split()))
