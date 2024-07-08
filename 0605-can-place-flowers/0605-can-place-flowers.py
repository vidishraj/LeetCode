class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ##Start from the beginning
        av= 0 
        if len(flowerbed)==1 and flowerbed[0]==0 and n==1:
            return True
        for i in range(len(flowerbed)):
            if i==0 and len(flowerbed)>1 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[0]= 1
                av+=1
            elif i==len(flowerbed)-1 and len(flowerbed)>1 and flowerbed[-2]==0 and flowerbed[i]==0:
                flowerbed[-1]=1
                av+=1
            elif i-1>0 and i+1<len(flowerbed) and flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                av+=1        
        if av>=n:
            return True
        return False