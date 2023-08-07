# Horizontal:
    listSum.extend([sum(lines) for lines in matrix])

# Vertical:
    for col in range(Size):
        listSum.append(sum(row[col] for row in matrix))

#Diagonal
    Diagonal1 = 0
    for i in range(0, Size):
        Diagonal1 += matrix[i][i]
    listSum.append(Diagonal1)

    Diagonal2 = 0
    for i in range(Size - 1, -1, -1):
        Diagonal2 += matrix[i][i]
    listSum.append(Diagonal2)

    if len(set(listSum)) > 1:
        return False
    return True


m = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
print(magic_Sq(m));

m = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(magic_Sq(m));

m = [[2, 7, 6], [9, 5, 1], [4, 3, 7]]
print(magic_Sq(m));
