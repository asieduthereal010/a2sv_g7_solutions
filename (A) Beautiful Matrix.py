matrix = []
for _ in range(5):
    matrix.append([int(x) for x in input().split(" ")])

one_coordinate = (0,0);

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            one_coordinate = (1+i,j+1)

print(abs(one_coordinate[0]-3)+abs(one_coordinate[1]-3))
