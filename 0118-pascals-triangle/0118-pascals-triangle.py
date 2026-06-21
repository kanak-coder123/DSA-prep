class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
            
        x = []
        x.append([1])
        
        for i in range(numRows - 1):
            n = i + 1
            y = [1] * (n + 1)
            val = 1
            
            for j in range(1, n + 1):
                val = val * (n - j + 1) // j
                y[j] = val
                
            x.append(y)
            
        return x

