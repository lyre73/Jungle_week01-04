# 히스토그램에서 가장 큰 직사각형
import sys

def histogram():
    for line in sys.stdin.readlines():
        data = list(map(int, line.split()))
        # print(data)
        if data[0] == 0:
            return
        elif data[0] == 1:
            print(data[1])
            continue
        
        data.append(0)
        stack = [(0, 0)]
        area = 0

        for i in range(1, data[0] + 2):
            # print(i)
            if stack[-1][0] < data[i]:
                stack.append((data[i], i))
            else:
                while stack[-1][0] > data[i]:
                    temp = stack.pop()
                    area = max(area, temp[0] * (i - temp[1]))
                if data[i] > stack[-1][0]:
                    stack.append((data[i], temp[1]))
            # print(i, stack, area)
        # area = max(area, stack[-1][0] * (data[0] + 1 - stack[-1][1]))
        print(area)
histogram()