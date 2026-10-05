class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        if len(s1) > len(s2):
            return False
        count_s1 = {}
        
        for c in s1:
            count_s1[c] = count_s1.get(c, 0)+1
        print(count_s1)

        len_s2 = len(s2)
        count_window = {}
        l = 0
        for r in range(0 , len(s1)):
            count_window[s2[r]] = count_window.get(s2[r],0)+1
        if count_s1 == count_window:
                return True
        for r in range(len(s1),len(s2)):
            
                count_window[s2[l]] = count_window.get(s2[l])-1
                if count_window[s2[l]] == 0:
                    del count_window[s2[l]]
                l+=1
                count_window[s2[r]] = count_window.get(s2[r],0)+1
                if count_s1 == count_window:
                    return True

        return False
