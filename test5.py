def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            return answer


print(solution(12))
