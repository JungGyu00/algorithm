def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer


print(solution(12))


# def solution(n):
#     answer = 0
#     i = 1
#     while True:
#         if n % i == 0:
#             answer = (n/i) + i
#             i += 1
#         else:
#             break
#     return answer


# print(solution(12))
