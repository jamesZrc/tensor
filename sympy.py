import numpy as np
from numpy.linalg import solve

target = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
size = len(target)

xy = []
for i in range(size):
    x = []
    for j in range(size):
        x.append((i + 1) ** j)
    xy.append(x)

a = np.mat(xy)
b = np.mat(target).T
result = solve(a, b)
print(result)

test = 15
test_x = []
for j in range(size):
    test_x.append(test ** j)

test_y = 0
for i in range(size):
    test_y = test_y + test_x[i] * result[i][0]

print(test_y)
