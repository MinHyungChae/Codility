
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections


def solution(A):
    # write your code in Python 3.6
    dict_A = dict(collections.Counter(A))
    
    for key, value in dict_A.items():
        if (value % 2) != 0:
            return key
