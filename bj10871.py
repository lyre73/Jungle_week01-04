N, X = input().split()

A = [int(i) for i in input().split()]

for i in range(int(N)):
    if A[i] < int(X):
        print(A[i], end=' ')