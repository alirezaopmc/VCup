_i = int(input("which testcase? "))

f = open(f'in/input{_i}.txt', 'r')

lines = f.read().split('\n')

n, q = map(int, lines[0].split())

for i in range(q):
    line = lines[i+1]

    if line == '?':
        print(n)
        continue

    t = int(line[2:])
    # print(f't = {t}, n = {n}')
    
    if line[0] == '+':
        n += t
    elif line[0] == '-':
        n -= t
    elif line[0] == '*':
        n *= t
    elif line[0] == '/':
        n //= t
    elif line[0] == '%':
        n %= t
    elif line[0] == '^':
        n **= t