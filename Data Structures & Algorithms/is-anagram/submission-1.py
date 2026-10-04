class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countStr1 = {}
        countStr2 = {}

        for c in s:
            if(c not in countStr1):
                countStr1[c]=0
            countStr1[c] += 1
        # print(countStr1)
        
        for c in t:
            if(c not in countStr2):
                countStr2[c]=0
            countStr2[c] += 1
        # print(countStr2)

        return countStr1 == countStr2
        
        if (len(countStr1) == len(countStr2)):
            for c in countStr1:
                if(c not in countStr2): return False
                if(countStr1[c] != countStr2[c]): return False
            return True
        return False
        