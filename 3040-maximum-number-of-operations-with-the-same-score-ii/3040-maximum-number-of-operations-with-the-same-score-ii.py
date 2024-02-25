from collections import deque


class Solution:
    maximumOps: int
    startEndDict: dict

    def recOptions(self, q: deque, total: int, ops: int, start: int, end: int):
        # print(start, end, total, ops, self.maximumOps)
        if start>end:
            return
        if self.startEndDict.get(total) is not None:
            if self.startEndDict[total].get((start, end)) is True:
                return
        if ops > self.maximumOps:
            self.maximumOps = ops
        if start<=len(q)-2:
            frontOps = q[start] + q[start+1]
            if frontOps == total:
                self.recOptions(q, total, ops + 1, start + 2, end)
        if end>1:
            backOps = q[end-1] + q[end-2]
            if backOps == total:
                self.recOptions(q, total, ops + 1, start, end - 2)
        if start<len(q)-1 and end>0 and start<end:
            altOps = q[start] + q[end-1]
            if altOps == total:
                self.recOptions(q, total, ops + 1, start + 1, end - 1)
        if self.startEndDict.get(total) is None:
            self.startEndDict[total] = {}
        self.startEndDict[total][(start, end)] = True

    def maxOperations(self, nums: list[int]) -> int:
        self.maximumOps = 0
        self.startEndDict = {}
        q = deque()
        for num in nums:
            q.append(num)

        if len(q) > 0:
            # front operations
            total = q[0] + q[1]
            self.startEndDict[total]={}
            self.recOptions(q, total, 1, 2, len(q))
            # back operation
            total = q[-1] + q[-2]
            if self.startEndDict.get(total) is None:
                self.startEndDict[total]={}
            self.recOptions(q, total, 1, 0, len(q) - 2)
            # alt operation
            total = q[0] + q[-1]
            if self.startEndDict.get(total) is None:
                self.startEndDict[total]={}
            self.recOptions(q, total, 1, 1, len(q) - 1)
        return self.maximumOps
