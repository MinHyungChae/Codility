# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # convert N into binary and remove 0b
    binaryN = bin(N)[2:]
    oneList = list()
    gapList = list()
    
    gapList.append(0)
    
    for index, value in enumerate(binaryN):
        if value == '1':
            oneList.append(index)
            
    
    for index in range(len(oneList)-1):
        gapList.append(oneList[index+1] - oneList[index] - 1)
    
    return max(gapList)