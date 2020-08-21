def solution(X,A):

    A.sort()
    full = list(range(1,X+1))
    iter = 0
    for i in A:
        if i in full:
            full.remove(i)
        #print(str(iter) + '---' + str(i))
        #print(full)
        if full == []:
            return iter
        iter += 1
    return -1

A = [3,2,4,5,1,6]
X = 2

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(X,A))
