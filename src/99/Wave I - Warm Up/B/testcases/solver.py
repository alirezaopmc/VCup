_i = int(input("which testcase? "))

f = open(f'in/input{_i}.txt', 'r')

lines = f.read().split('\n')

n = int(lines[0])

print(f'[{n * "o"}{(7-n) * "-"}]')
print('   \|/')
print('    |')
print('    |')
print('    |')