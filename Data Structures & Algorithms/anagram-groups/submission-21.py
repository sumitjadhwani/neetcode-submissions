class Solution:
    def groupAnagrams(self, inp: List[str]) -> List[List[str]]:
        res_dict = {}
        op = []
        
        for word in inp:
            sort_word = ''.join(sorted(word))
            
            if sort_word not in res_dict:
                res_dict[sort_word]=[word]
            else:
                res_dict[sort_word].append(word)
        
        for itr in res_dict.values():
            op.append(itr)
        
        return op