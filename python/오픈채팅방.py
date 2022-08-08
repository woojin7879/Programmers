def solution(record):
    answer = []
    dictionary = {}
    for i in record:
        if len(i.split(' ')) == 3:
            dictionary[i.split(' ')[1]] = i.split(' ')[2]
    for i in record:
        if i.split(' ')[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dictionary[i.split(' ')[1]])
        if i.split(' ')[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dictionary[i.split(' ')[1]])
    return answer