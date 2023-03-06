class id:
    def __init__(self):
        self.unique_id = 1
    def newID(self):
        rt = self.unique_id
        self.unique_id+=1
        return rt
