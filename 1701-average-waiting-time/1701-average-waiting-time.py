class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        Iterate through the list. Find the 
        
        """
        startTime = customers[0][0]
        waitingTime = 0
        for customer in customers:
            waitingTimeForPrev = startTime - customer[0]
            if waitingTimeForPrev<0:
                startTime = customer[0]
                waitingTimeForPrev = 0
            waitingTimeForOwn = customer[1]
            totalWaitingTime = waitingTimeForPrev+waitingTimeForOwn
            waitingTime += totalWaitingTime
            startTime = startTime+waitingTimeForOwn
        return waitingTime/len(customers)