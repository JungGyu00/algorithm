def solution(x):
    answer = list(str(x))
    h = 0
    for i in answer:
        h += int(i)
    if x % h == 0:
        return True
    return False