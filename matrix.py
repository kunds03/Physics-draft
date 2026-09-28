A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

C = []

for i in range(2):
    row = []
    for j in range(2):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print(C)

D = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            D[i][j] += A[i][k] * B[k][j]

print(D)