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


# *4 하고 리턴한다는 첫 발상을 적용하는 데 성공한 경우
# def z(n, r, c):
#     if n == 0 :
#         return 0
#     return 4 * z(n-1, r//2, c//2) + 2 * (r % 2) + c % 2
#     """ 37의 경우
#     n = 1: 4 * 0 + 2 * 1 + 1 > (2) 2
#     n = 2: 4 * 2 + 2 * 0 + 1 > (1) 9
#     n = 3: 4 * 9 + 2 * 0 + 1 > (1) 37
#     """

# N, r, c = map(int, (input().split()))
# print(z(N, r, c))