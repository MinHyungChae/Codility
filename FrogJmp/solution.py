# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    
    gap = Y - X
    if gap == 0:
        return 0
        
    if gap % D == 0:
        return gap // D
    else:
        return gap // D + 1
