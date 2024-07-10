import queue


class Solution:
    def victim(self, killer):
        if killer == "R":
            return "D"
        return "R"

    def predictPartyVictory(self, senate: str) -> str:
        """
            The order seems to matter a lot 
            Lets think 
            In each round, the first R will eliminate the first D and the first D will eliminate the first R
            This will go on till the last person is left
        """
        
        #Corner case
        if len(senate)==1:
            if senate[0]=="D":
                return "Dire"
            return "Radiant"
        
        q = queue.Queue()
        dCount = 0
        rCount = 0
        for senator in senate:
            # init queue
            if senator == "D":
                dCount += 1
            else:
                rCount += 1
            q.put(senator)
        print(dCount, rCount)
        # Killing begins
        rKillsRemaining = 0
        dKillsRemaining = 0
        rKills = 0
        dKills = 0
        # keep track of killings?
        while q.qsize() > 1:
            curr = q.get()
            if rKillsRemaining==0 and dKillsRemaining==0:
                nextKill = self.victim(curr)
                if nextKill == "R":
                    rKillsRemaining+=1
                else:
                    dKillsRemaining+=1
                q.put(curr)  # put winner back
            elif curr =="R" and rKillsRemaining>0:
                rKillsRemaining-=1
                rKills+=1
            elif curr=="D" and dKillsRemaining>0:
                dKillsRemaining-=1
                dKills+=1
            else:
                nextKill = self.victim(curr)
                if nextKill == "R":
                    rKillsRemaining+=1
                else:
                    dKillsRemaining+=1
                q.put(curr) #put the item back
            if rKills == rCount:
                return "Dire"
            if dKills == dCount:
                return "Radiant"
        if q.queue[0] == "D":
            return "Radiant"
        return "Dire"
