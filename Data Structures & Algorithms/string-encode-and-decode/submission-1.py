class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            str = str + ';'
            res += str
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)

        temp =""
        for c in s:
            if(c != ';'):
                temp+=c
            if(c == ';'):
                res.append(temp)
                temp=""
        return res