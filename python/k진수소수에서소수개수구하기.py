def solution(n, k):
    answer = 0
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    newn = rev_base[::-1]
    splitn = newn.split('0')
    splitn = list(filter(lambda x: x != '', splitn))
    for i in splitn:
        if getPrimeNum(int(i)):
            answer += 1
    return answer

def getPrimeNum(n):
    if n == 1 :
        return False
    elif n == 2 :
        return True
    m = int(n ** 0.5) + 1
    for i in range(2, m):
        if n % i == 0 :
            return False
    return True

print(solution(437674, 3))
print(solution(110011, 10))