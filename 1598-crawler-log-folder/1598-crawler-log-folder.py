class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depthLevel = 0
        for log in logs:
            if log =="../":
                if depthLevel>0:
                    depthLevel-=1
            elif log!="./":
                depthLevel+=1
        if depthLevel<0:
            return 0
        return depthLevel