# 잃어버린 괄호
import sys
input = sys.stdin.readline

expression = input().rstrip()
x = expression.split('-')

temp = sum(map(int, x[0].split('+')))

for exp in x[1:]:
    temp -= sum(map(int, exp.split('+')))
print(temp)