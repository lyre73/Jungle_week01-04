heights = [int(input()) for _ in range(9)]
height_over = sum(heights) - 100

for i in range(8):
    for j in range(i+1, 9):
        if heights[i] + heights[j] == height_over:
            del heights[i]
            del heights[j-1]
            for height in sorted(heights):
                print(height)
            exit()