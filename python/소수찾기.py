from itertools import permutations
def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def solution(numbers):
    answer = []
    num = list(numbers.strip())
    permut = []
    newnum = []
    for i in range(1,len(num) + 1):
        permut += list(permutations(num, i))
    for p in permut:
        newnum.append("".join(p))
    for n in newnum:
        if prime(int(n)) and int(n) not in answer:
            answer.append(int(n))
    return len(answer)