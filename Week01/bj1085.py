xywh = [int(i) for i in input().split()]
list1 = sorted([xywh[0], xywh[1], xywh[2]-xywh[0], xywh[3]-xywh[1]])

print(list1[0])

# another way to solve 

# xywh = [int(i) for i in input().split()]
# print(min([xywh[0], xywh[1], xywh[2]-xywh[0], xywh[3]-xywh[1]]))