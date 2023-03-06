def med3(a, b, c):
    """a, b, c의 중앙값을 구하여 반환"""
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print(f'중앙값 {med3(2,2,2)}')