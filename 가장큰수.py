def solution(numbers):
    answer = ''
    numbers_str = [str(num) for num in numbers]  
    numbers_str.sort(key = lambda item: item * 3, reverse = True)
    for i in numbers_str:
        answer += i
    return str(int(answer))