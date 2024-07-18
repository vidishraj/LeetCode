class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        We need three heaps instead of two.
        keep the middle elements in a heap too. 
        """
        firstIndex = candidates
        lastIndex = len(costs) - candidates
        if firstIndex>=lastIndex:
            firstIndex = math.ceil(len(costs)/2)
            lastIndex = firstIndex
        leftHeap =[costs[i] for i in range(firstIndex)]
        rightHeap = [costs[i] for i in range(lastIndex, len(costs))]
        ##Middle heap should be kept with priority of Index. if left side has smaller element, prefer that, else right side
        middleHeap = [[costs[i], i] for i in range(firstIndex, lastIndex)]
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)
        heapq.heapify(middleHeap)
        # print(leftHeap, rightHeap)
        lastIndex-=1
        res = 0
        for i in range(k):
            if firstIndex<=lastIndex:
                if leftHeap[0]<rightHeap[0]:
                    res+=heapq.heapreplace(leftHeap, costs[firstIndex])
                    firstIndex+=1
                elif rightHeap[0]<leftHeap[0]:
                    res+=heapq.heapreplace(rightHeap, costs[lastIndex])
                    lastIndex-=1
                else:
                    smallestEl = middleHeap[0]
                    smallestElIndex = smallestEl[1]
                    if smallestElIndex-firstIndex<lastIndex-smallestElIndex:
                        res+=heapq.heappop(leftHeap)
                        heapq.heappush(leftHeap,costs[firstIndex])
                        firstIndex+=1
                    else:
                        res+=heapq.heappop(rightHeap)
                        heapq.heappush(rightHeap, costs[lastIndex])
                        lastIndex-=1
                    heapq.heappop(middleHeap)
            else:
                if len(leftHeap)>0 and len(rightHeap):
                    if leftHeap[0]<rightHeap[0]:
                        res+=heapq.heappop(leftHeap)
                    else:
                        res+=heapq.heappop(rightHeap)
                elif len(rightHeap)>0:
                    res+=heapq.heappop(rightHeap)
                else:
                    res+=heapq.heappop(leftHeap)
            
        return res