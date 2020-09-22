# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # 서로 다른 정수로 이루어진 배열
    # N 개로 이루어져있고, 범위는 1 ~ (N+1) 까지임
    real = [i for i in range(1, len(A)+2)]
    answer = list(set(real) - set(A)).pop()
    
    return answer
    
