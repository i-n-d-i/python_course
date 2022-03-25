def minor(matrix, num):
    answer = []
    for row in matrix[1:]:
        row2 = [row[i] for i in range(len(row)) if i != num]
        answer.append(row2)
    return answer

def determinant(m):
    answer = 0
    if len(m) == 3:
        return m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] - m[0][2] * m[1][1] * m[2][0] - m[0][0] * m[1][2] * m[2][1] - m[0][1] * m[1][0] * m[2][2]
    for i in range(len(m)):
        answer = answer + ((-1) ** i) * m[0][i] * determinant(minor(m, i))
    return answer

matrix = eval(input())
print(determinant(matrix))
