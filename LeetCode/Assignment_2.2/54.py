class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        spi = []
        while matrix and matrix[0]:
            spi += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    if row:
                        spi.append(row.pop())
            if matrix:
                spi += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spi.append(row.pop(0))
        return spi