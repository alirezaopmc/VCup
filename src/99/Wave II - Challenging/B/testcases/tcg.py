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
    c = []
    for i in range(length):
        c.append(random.choice(salt))
    return str(''.join(c))
    

# Test-case generator template
# Example problem: Take n and m in first line
# and take n elements in second line
# print sum of n elements mod m

count = 0

def giveRandomInput():
    n = randInt(min = 2, max = 20)[0]
    a = [giveRandomString('01', 7) for i in range(n)]
    return (n, a)

def solveOut(inputs):
    (n, a) = inputs

    lines = [""] * 5
    lines[1] = "   \|/   " * n
    lines[2] = "    |    " * n
    lines[3] = lines[2]
    lines[4] = lines[2]

    for i in range(n):
        lines[0] += '[{}]'.format(a[i])
    lines[0] = lines[0].replace('0', '-')
    lines[0] = lines[0].replace('1', 'o')

    ans = ""
    for i in range(5):
        ans += lines[i] + '\n'

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
    (n, a) = inputs

    inString = '{}\n'.format(n)
    inString += ' '.join(a)
    
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")