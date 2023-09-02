def solution(price, money, count):
    a = sum([price*cnt for cnt in range(1, count+1)])
    if money - a >= 0:
        return 0
    else:
        return abs(money - a)