def solution(s):
    answer = list("abcdefgfhijklmnopqrstuvwxyz")
    for i in s.lower():
        if i in answer or len(s) not in (4, 6):
            return False
    return True

