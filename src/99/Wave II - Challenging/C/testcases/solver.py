_i = int(input("which testcase? "))

f = open(f'in/input{_i}.txt', 'r')

lines = f.read().split('\n')

r = lines[0]
w = lines[1]

ind = [-1] * 26
for i in range(26):
    ind[ord(r[i]) - ord('a')] = (i - ord(r[i]) + ord('a')) ** 2

ans = 0
for ch in w:
    ans += ind[ord(ch) - ord('a')]

print(ans)