def solution(numbers):
    answer = 45 
    for i in range(0, len(numbers)):
        answer = answer - numbers[i]
    return answer

numbers = [5,8,4,0,6,7,9]
answer = solution(numbers)
print(answer)