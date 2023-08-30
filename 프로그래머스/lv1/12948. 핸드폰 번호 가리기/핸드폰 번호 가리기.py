def solution(phone_number):
    answer = []
    for i, x in enumerate(reversed(phone_number)):
        if i >= 4:
            answer.append('*')
        else:
            answer.append(x)
    return ''.join(n for n in reversed(answer))