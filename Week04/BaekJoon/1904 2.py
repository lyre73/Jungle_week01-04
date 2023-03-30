# 01타일
a, b = 0, 1
for _ in range(int(input())):
    a, b = b, (a + b) % 15746
print(b)