import queue
class RecentCounter:
    q: queue.Queue
        
    def __init__(self):
        self.q = queue.Queue()
    
    def ping(self, t: int) -> int:
        self.q.put(t)
        
        if t - self.q.queue[0]>3000:
            while t - self.q.queue[0]>3000:
                self.q.get()
        return self.q.qsize()


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)