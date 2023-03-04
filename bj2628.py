import sys

x, y = map(int, sys.stdin.readline().split())
horCut = [x]
verCut = [y]
for i in range(int(sys.stdin.readline())):
    flag, line = map(int, sys.stdin.readline().split())
    if flag == 1:
        horCut.append(line)
    else:
        verCut.append(line)
horCut.sort()
verCut.sort()

hor = [horCut[0]]
ver = [verCut[0]]
for i in range(len(horCut)-1):
    hor.append(horCut[i+1]-horCut[i])
for i in range(len(verCut)-1):
    ver.append(verCut[i+1]-verCut[i])
print(max(hor)*max(ver))