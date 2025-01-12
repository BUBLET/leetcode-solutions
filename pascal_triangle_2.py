from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        res_add = []
        i = 0

        while i < rowIndex+1:
            res_add = []
            if len(res) == 0:
                res_add = [1]
                res.append(res_add)
                i += 1
            elif len(res) == 1:
                res_add = [1, 1]
                res.append(res_add)
                i += 1
            else:
                res_add.append(1)
                for j in range(len(res[-1])-1):
                    res_add.append(res[-1][j]+res[-1][j+1])
                res_add.append(1)
                res.append(res_add)
                i += 1
        return res_add
    