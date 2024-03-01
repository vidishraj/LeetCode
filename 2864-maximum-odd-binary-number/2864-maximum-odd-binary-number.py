class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # binary is 1,2,4,8,9,
        countOnes=0
        for letter in s:
            if letter=='1':
                countOnes+=1
        onesToInsert=countOnes-1
        zeroesToInsert=len(s)-countOnes
        solution=""
        while onesToInsert>0:
            solution+='1'
            onesToInsert-=1
        while zeroesToInsert>0:
            solution+='0'
            zeroesToInsert-=1
        solution+='1'
        return solution