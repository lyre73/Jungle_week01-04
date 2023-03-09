A = int(input())
B = int(input())
C = int(input())

ans = str(A*B*C)

for i in range(10):
    print(ans.count(str(i)))