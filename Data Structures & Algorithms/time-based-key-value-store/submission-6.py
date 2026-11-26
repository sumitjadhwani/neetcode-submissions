class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [[value, timestamp]]
        else:
            self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        else:
            res = ""
            values = self.timemap[key]
            l, r = 0, len(values)-1           
            while l<=r:
                mid = (l+r)//2
                if values[mid][1] <= timestamp:
                    res = values[mid][0]        #valid timestamp save it
                    l = mid+1
                else:
                    r = mid -1
            return res
t = TimeMap()

# t.set('alice', 'happy',1)

# print(t.get('alice',1))