class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for c in s1:
            count_s1[c] = count_s1.get(c, 0)+1
        print(count_s1)

        len_s1 = len(s1)

        for l in range(0,len(s2)-len_s1+1):
            count_window = {}
            for r in range(l,l+len_s1):
                count_window[s2[r]] = count_window.get(s2[r],0)+1
            if count_s1 == count_window:
                return True
            continue
        return False
