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
        latest = None
        for val,time in val_list:
            if time <= timestamp:
                latest = val
        return latest if latest else ""

        
