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
    return C

def giveRandomString(salt, length):
    s = []
    for i in range(length):
        s.append(random.choice(salt))
    return ''.join(s)
    

# Test-case generator template
# Example problem: Take n and m in first line
# and take n elements in second line
# print sum of n elements mod m

alphabet = 'abcdefghijklmnopqrstuvwxyz'

count = 0

def giveRandomInput():
    s = giveRandomString(alphabet, randInt()[0])
    t = giveRandomString(alphabet, randInt()[0])
    return (s, t)

def solveOut(inputs):
    (s, t) = inputs
    
    ans = list(t)
    off = 0
    for i in range(len(ans)):
        ans[i] = chr(ord('a') + (ord(t[i]) + ord(s[off]) - 2 * ord('a') + 1) % 26)
        off = (off + 1) % len(s)

    return str(''.join(ans))

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
    (s, t) = inputs

    inString = '{}\n{}'.format(s, t)
    
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")