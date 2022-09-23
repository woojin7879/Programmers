import math

def timeMap(date):
    h, m = map(int, date.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees
    
    dic = {}

    for r in records:
        time, number, history = r.split()
        number = int(number)
        
        if number in dic:
            dic[number].append([timeMap(time), history])
        else:
            dic[number] = [[timeMap(time), history]]
    
    sortDic = sorted(dic.items(), key=lambda x : x[0])
    
    for key, val in sortDic:
        t = 0

        for rr in val:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]

        if val[-1][1] == "IN":
            t += 1439
        
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t-dt) / ut) * uf)        

    return answer