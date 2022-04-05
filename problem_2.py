def solution(n=4e6):
    s = 0
    prev2, prev = 0, 1

    while prev < n:
        prev2, prev = prev, prev2 + prev

        if prev % 2 == 0:
            s += prev

    return s


# 4613732
print(solution()) 
