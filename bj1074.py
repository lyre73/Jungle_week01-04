# def zee(N, r, c):
#     if N < 1:
#         return 0
#     else:
#         half_line = 2 ** (N - 1) # 한 변의 절반
#         if r >= half_line:
#             flagRow = 1
#         else:
#             flagRow = 0
#         if c >= half_line:
#             flagCol = 1
#         else:
#             flagCol = 0
#         return (half_line ** 2) * (flagRow * 2 + flagCol) + zee(N-1, r - flagRow * half_line, c - flagCol * half_line)
        
# N, r, c = map(int, (input().split()))
# print(zee(N, r, c))

def zee(N, r, c):
    if N < 1:
        return 0
    else:
        quadrant = [[0, 1], [2, 3]]
        half_line = 2 ** (N - 1)
        x = r // half_line
        y = c // half_line
        return (half_line ** 2) * quadrant[x][y] + zee(N-1, r % half_line, c % half_line)
        
N, r, c = map(int, (input().split()))
print(zee(N, r, c))