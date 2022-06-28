import math
def solution(w,h):
    answer = w * h
    answer -= w + h
    answer += math.gcd(w, h)
    return answer