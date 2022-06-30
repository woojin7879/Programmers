def solution(phone_book):
    answer = True
    dic = {}
    for i in phone_book:
        dic[i] = 1
    for p in phone_book:
        temp = ""
        for j in p:
            temp += j
            if temp in dic and temp != p:
                return False
    return True

    #답지보고풀었는데 신기하다 생각방식이