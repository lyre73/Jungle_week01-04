# 가장 가까운 두 점
# https://my-coding-notes.tistory.com/103 참고(거의 복붙)

import sys
input = sys.stdin.readline

n = int(input())
pts = [tuple(map(int, line.split())) for line in sys.stdin.readlines()]
pts.sort()
# print(pts)

def square_dist(pt1, pt2):
    return (((pt1[0] - pt2[0]) ** 2) + ((pt1[1] - pt2[1]) ** 2))

def nearest(start, end):
    if start == end:
        return float('inf')
    
    if end - start == 1:
        return square_dist(pts[start], pts[end])
    
    mid = (start + end) // 2
    min_dist = min(nearest(start, mid), nearest(mid, end))

    target_pts = []
    for i in range(start, end+1):
        if (pts[mid][0] - pts[i][0]) ** 2 < min_dist:
            target_pts.append(pts[i])

    target_pts.sort(key=lambda x: x[1])

    for i in range(len(target_pts)):
        for j in range(i+1, len(target_pts)):
            if (target_pts[i][1] - target_pts[j][1]) ** 2 < min_dist:
                min_dist = min(min_dist, square_dist(target_pts[i], target_pts[j]))
            else:
                break

    return min_dist

print(nearest(0, n-1))