class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=s
            res+='\n'
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        temp=""
        for i in range(0,len(s),1):
            # print(s[i])
            if s[i]=='\n':
                res.append(temp)
                temp=""
            else:
                temp+=(s[i])
        return res