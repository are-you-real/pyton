def solution(N):
    nBin = bin(N)[2:]
    print(nBin)
    ile = 0
    max = 0
    for i in nBin:
        if i == '0':
            ile = ile + 1
        elif max < ile:
            max = ile
            ile = 0
        else:
            ile = 0
    return max

print(solution(10))
