def solution(t, p):
    answer = 0
    cnt = 0
    for i in range(len(t)-(len(p)-1)):
        answer = t[i:len(p)+i]
        if answer <= p:
            cnt += 1
    return cnt