from itertools import permutations
def calc(op, exp):
    if not op:
        return str(exp)
    else:
        exp_split = exp.split(op[0])
        tmp = []
        for e in exp_split:
            tmp.append(calc(op[1::],e))
        return str(eval(op[0].join(tmp)))
def solution(expression):
    answer = []
    operator = ['+','-','*']
    for o in permutations(operator, 3):
        answer.append(abs(int(calc(o,expression))))      
    return max(answer)