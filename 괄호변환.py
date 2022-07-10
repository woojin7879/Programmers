def divide(w):
    left = 0
    right = 0
    for i in w:
        if i == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return w[:left + right:], w[left + right::]
        
def verify(u):
    left = 0
    right = 0
    for i in u:
        if i == '(':
            left += 1
        else:
            right += 1
        if right > left:
            return False
    return True

def solution(p):
    answer = ''
    if len(p) == 0:
        return p
    u, v = divide(p)
    if verify(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:-1:]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer
            
            
    return answer