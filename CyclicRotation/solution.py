# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if len(A) <= 1 or K == 0 or len(list(set(A))) <= 1:
        return A
    
    step = K % len(A)
    answer = [0 for i in range(len(A))]
    
    for now_idx in range(len(A)):
        next_idx = now_idx + step
        
        if next_idx >= len(A):
            next_idx -= len(A)
        
        answer[next_idx] = A[now_idx]
    
    return answer
