class Solution:
    def groupAnagrams(self, inp: List[str]) -> List[List[str]]:
        op = {}
    
        for s in inp:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')]+=1
            
            if tuple(count) not in op:
                op[tuple(count)]=[s]
            else:
                op[tuple(count)].append(s)
        
        return list(op.values())