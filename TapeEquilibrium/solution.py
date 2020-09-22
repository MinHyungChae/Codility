# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# O(N) 으로 최대한 맞춰보기! sum 은 N**2 를 유발할 수 있다!

def solution(A):
    # write your code in Python 3.6
    sum_second = sum(A)
    sum_first = 0
    answer = None
    
    for i in range(len(A)-1):
        sum_second -= A[i]
        sum_first += A[i]
        
        if answer == None:
            answer = abs(sum_second - sum_first)
        else:
            answer = min(answer, abs(sum_second - sum_first))
            
    return answer
