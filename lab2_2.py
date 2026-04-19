from typing import List

def jump_search_quadratic(arr: List[int], target: int) -> int:
    """Search sorted arr using jumps of sizes 1,4,9,16,... quadratic increments."""
    n = len(arr)
    if n == 0:
        return -1

    step = 1
    prev = 0
    steps = 0
    # Jump phase
    while prev < n and arr[prev] < target:
        steps+=1
        if arr[prev] == target:
            return steps

        next_index = prev + step
        if next_index >= n:
            break

        if arr[next_index] >= target:
            # do linear search from prev+1 to next_index
            for i in range(prev + 1, min(next_index + 1, n)):
                steps+=1
                if arr[i] == target:
                    return steps
                if arr[i] > target:
                    return -1
            return -1

        prev = next_index
        step += 2  # next jump difference will grow to 3,5,7,... making square increments

    # If we exit because we overshot the end or next_index beyond n, do linear from prev+1
    for i in range(prev, n):
        if arr[i] == target:
            return steps
        if arr[i] > target:
            return -1

    return -1

for i in range(15):
    list = []
    for j in range(i**2):
        list.append(j)
    average = 0
    for j in range((i**2)-1):
        average += jump_search_quadratic(list,j)
    average = average/ (i**2 | 1)
    print(i,average)