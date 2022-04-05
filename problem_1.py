# O(n) solution
# def solution(n=1000):
#     return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

# O(1) solution
def solution(n=1000):
    term = n - 1
    term3 = term // 3
    term5 = term // 5
    term15 = term // 15

    return (
        3 * term3 * (term3 + 1)
        + 5 * term5 * (term5 + 1)
        - 15 * term15 * (term15 + 1)
    ) // 2


# 233168
print(solution())
