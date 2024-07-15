matrix= [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]

def transpose(m):
    for row in range(len(m) // 2):
        for column in range(row, len(m) - row):
            source = (row, column)
            target = (column, len(m) - row - 1)
            temp = m[target[0]][target[1]]
            for i in range(0, 4):
                temp_2 = m[target[0]][target[1]]
                m[target[0]][target[1]] = temp
                if i == 4:
                    break
                source = target
                target = (source[1], len(m) - source[0] - 1)
                temp = temp_2
			
    return m

blah = transpose(matrix)

print(blah)

assert(transpose([]) == [])
assert(transpose([[1]]) == [[1]])