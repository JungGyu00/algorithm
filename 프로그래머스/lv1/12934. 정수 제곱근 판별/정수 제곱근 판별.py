def solution(n):
    answer = 0
    if n ** (1/2) == int(n ** (1/2)):
        answer = int(n ** (1/2)) + 1
        answer **= 2
    else:
        return -1
    return answer