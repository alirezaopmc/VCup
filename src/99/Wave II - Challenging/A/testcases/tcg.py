import random

# Utility functions
def arrayToString(arr: list):
    result: str = ""

    for i in range(len(arr)):
        if i + 1 < len(arr):
            result += "{} ".format(arr[i])
        else:
            result += "{}".format(arr[i])
    
    return result

def randInt(min = 1, max = 100, cnt = 1):
    result = []
    for i in range(cnt):
        result.append(random.randint(min, max))
    return tuple(result)

def matMul(A, B):
    n, m, k = len(A), len(B), len(B[0])
    C = [ [0 for j in range(k) ] for j in range(n) ]
    for i in range(n):
        for j in range(k):
            for t in range(m):
                x = A[i][t]
                y = B[t][j]
                C[i][j] += (x & y) + (x | y)
    return C;
    

# Test-case generator template
# Example problem: Take n and m in first line
# and take n elements in second line
# print sum of n elements mod m

count = 0

def giveRandomInput():
    n, m, k = randInt(max = 100, cnt = 3)
    A = [[ random.randint(-1000, 1000) for j in range(m) ] for i in range(n) ]
    B = [[ random.randint(-1000, 1000) for j in range(k) ] for i in range(m) ]
    return (n, m, k, A, B)

def solveOut(inputs):
    (n, m, k, A, B) = inputs

    C = matMul(A, B)

    ans = ""

    for i in range(n):
        for j in range(k):
            ans += '{} '.format(C[i][j])
        ans += '\n'

    return "{}".format(str(ans))

def makeInputs(inString, cnt):
    path = "./in/input" + str(cnt) + ".txt"
    f = open(path, "w+")
    f.write(inString)
    f.close()

def makeOutputs(outString, cnt):
    path = "./out/output" + str(cnt) + ".txt"
    f = open(path, "w+")
    f.write(outString)
    f.close()

# Manually add some inputs
# if "Case 1":
#     n = 3
#     a = [1, 11, 12]
#     x = 5
#     inputs = (n, a, x)
    
#     inString = "{} {}\n{}\n".format(
#         n, x,
#         arrayToString(a)
#     )
#     outString = solveOut(inputs)
    
#     count += 1
#     makeInputs(inString, count)
#     makeOutputs(outString, count)

# Automatically add inputs
for i in range(10):
    inputs = giveRandomInput()
    (n, m, k, A, B) = inputs

    inString = '{} {} {}\n'.format(n, m, k)
    for i in range(n):
        for j in range(m):
            inString += '{} '.format(A[i][j])
        inString += '\n'
    for i in range(m):
        for j in range(k):
            inString += '{} '.format(B[i][j])
        inString += '\n'
    
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")