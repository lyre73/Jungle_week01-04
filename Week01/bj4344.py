for C in range(int(input())):
    scores = [int(score) for score in input().split()]
    N = scores.pop(0)
    avg = sum(scores)/N
    over_avg = 0
    for score in scores:
        if score > avg:
            over_avg += 1
    print('%3.3f%%' % (over_avg/N*100))