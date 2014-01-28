class MultiArray:

    def __init__(self, array_a, array_b):
        self.array_a = array_a
        self.array_b = array_b

    def column(self, matrix, i):
        return [row[i] for row in matrix]

    def columns(self, matrix):
        result = []
        for col in range(len(matrix[0])):
            result.append(self.column(self.array_b, col))
        return result

    def multi_by_row(self, row):
        result = []
        for column in self.columns(self.array_b):
            sum = 0
            for num in range(len(self.array_a[row])):
                sum += self.array_a[row][num] * column[num]
            result.append(sum)
        return result

array_a = [[1,2,3],[4,5,6],[7,8,9]]
array_b = [[1,2,3],[4,5,6],[7,8,9]]

p1 = MultiArray(array_a, array_b)
p2 = MultiArray(array_a, array_b)
p3 = MultiArray(array_a, array_b)

result = [[],[],[]]

#cobegin
result[0].extend(p1.multi_by_row(0))
result[1].extend(p1.multi_by_row(1))
result[2].extend(p1.multi_by_row(2))
#coend

print result
