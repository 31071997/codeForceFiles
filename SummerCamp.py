s = []
for i in range(1, 1001):
    s.append(i)
l = ''.join(str(a) for a in s)
n = int(input())
print(l[n-1])