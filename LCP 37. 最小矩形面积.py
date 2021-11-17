from typing import List
import numpy as np

class Solution:
    def minRecSize(self, lines: List[List[int]]) -> float:
        points_x = []
        points_y = []
        for i in range(len(lines)):
            for j in range(i+1, len(lines)):
                try:
                    (x, y) = self.countPoint(lines[i], lines[j])
                except np.linalg.LinAlgError:
                    continue
                
                points_x.append(x)
                points_y.append(y)

        if len(points_x) <= 1:
            return 0

        return (max(points_x) - min(points_x)) * (max(points_y) - min(points_y))

    def countPoint(self, line1, line2):
        a1 = line1[0]
        a2 = line2[0]
        b1 = line1[1]
        b2 = line2[1]

        A = np.array([[a1,-1],[a2,-1]])
        b= np.array([[-b1],[-b2]])

        # print(np.linalg.solve(A,b))

        return np.linalg.solve(A,b)



lines = [[3,3],[3,0],[4,1]]

s = Solution()
print(s.minRecSize(lines))
