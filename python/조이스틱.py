def solution(name):
    answer = 0
    horizental = len(name) - 1
    for i, c in enumerate(name):
        answer += min(ord(c) - ord("A"), ord("Z") + 1 - ord(c))
    
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        horizental = min([horizental, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    answer += horizental
    
    return answer