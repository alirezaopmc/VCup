_i = int(input("which testcase? "))

f = open(f'in/input{_i}.txt', 'r')

lines = f.read().split('\n')

n, m, k = map(int, lines[0].split())
A = [[0 for j in range(m)] for i in range(n)]
B = [[0 for j in range(k)] for i in range(m)]

k = 1
for i in range(n):
    A[i] = list(map(int, lines[k].split()))
    k += 1

for i in range(m):
    B[i] = list(map(int, lines[k].split()))
    k += 1

def matMul(A, B):
    n, m, k = len(A), len(B), len(B[0])
    C = [ [0 for j in range(k) ] for j in range(n) ]
    for i in range(n):
        for j in range(k):
            for t in range(m):
                x = A[i][t]
                y = B[t][j]
                C[i][j] += (x & y) + (x | y)
    return C

C = matMul(A, B)
print(C)