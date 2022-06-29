from collections import deque
def solution(priorities, location):
    deq = deque(priorities)
    priorities.sort(reverse = True)
    answer = 0
    start = 0
    while deq:
        d = deq.popleft()
        if d < priorities[answer]:
            deq.append(d)
            if start == location:
                location += len(deq)
            start += 1
        else:
            print(d)
            answer += 1
            if start == location:
                return answer
            start += 1