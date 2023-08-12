class TimeMap(object):
    timeMapDict={}
    def __init__(self):
        self.timeMapDict={}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        DS->
        {
            "key":{
                    timeStampList=[]-> Naturally sorted list
                    "timeStamp"-> value
                    }
        }
        """
        if self.timeMapDict.get(key) is not None:
            #key exists
            self.timeMapDict[key]['timeStampList'].append(timestamp)
            self.timeMapDict[key][timestamp]=value
        else:
            self.timeMapDict[key]={
              'timeStampList' : [timestamp],
               timestamp:value
            }
        return

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        Timestamps are strictly increasing, Hence we can perform binary search on the number. If not, while doing binary
        search we can store the lowest difference
        how to do binary search for the loswer number?
        1, 2, 3, 4, 5, 6, 7,8,9
        """
        if self.timeMapDict.get(key) is not None:
            timestampList=self.timeMapDict[key]['timeStampList']
            closestSolution=self.binarySearch(timestampList, timestamp)
           # print(closestSolution, key, timestamp, self.timeMapDict)
            if closestSolution ==-1:
                return ""
            else:
                return self.timeMapDict[key][closestSolution]
        return ""

    def binarySearch(self, timestampList, key):
        """
        does binary search and then either return the element or returns the closest element
        :return: element or the closest one
        """
       # print(timestampList, key)
        difference=10**7+1
        low=0
        solution=-1
        high=len(timestampList)-1
        mid=int((low+high)//2)
        while low<=high:
            # if( key==4):
            #     print(low, high, mid)
            if timestampList[mid]==key:
                return key
            elif abs(timestampList[mid]-key)<difference and timestampList[mid]<key:
                solution=timestampList[mid]
            if timestampList[mid]>key:
                high=mid-1
            if timestampList[mid]<key:
                low=mid+1
            mid=int((low+high)//2)
       # print(solution)
        if solution>key:
            return -1
        return solution


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)