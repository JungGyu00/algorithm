def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
# x의 첫 번째 인자 x[n] 기준으로 strings 리스트를 오름차순 정렬 후
# x의 두 번째 인자 x 기준(앞선 문자열이 앞쪽에 위치하도록)으로 오름차순 정렬
