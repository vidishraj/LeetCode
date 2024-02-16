class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ##essentially have to group intervals together 
        points.sort()
        result = []
        index = 1
        result = [points[0]]
        while(index<len(points)):
            if points[index][0]<=result[-1][1]:
                result[-1][1]=min(result[-1][1], points[index][1])
                index+=1
            else:
                result.append(points[index])
                index+=1
        return len(result)
            