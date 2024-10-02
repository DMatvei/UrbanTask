def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        line = []
        for j in range(m):
            line.append(value)
        matrix.append(line)

    return matrix


print(get_matrix(2, 2, 10))