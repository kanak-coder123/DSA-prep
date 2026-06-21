class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            val = 1 

            for j in range(i):
                val = val * (i - j) // (j + 1)
                row[j + 1] = val

            triangle.append(row)

        return triangle
