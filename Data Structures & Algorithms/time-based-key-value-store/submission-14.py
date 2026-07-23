class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))
      
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        val_list = self.store[key]
        candidate = None
        l,r = 0, len(val_list)-1
        while l<=r:
            mid = (l + r) //2
            mid_time = val_list[mid][1]
            mid_candidate = val_list[mid][0]
            if mid_time <= timestamp:
                candidate = mid_candidate
            if mid_time > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return candidate if candidate else ""
