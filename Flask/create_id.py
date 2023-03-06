from datetime import datetime
import random
class id:
    def __init__(self):
        self.unique_id = 1
    def newID(self):
        rt = datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randrange(0, 9))
        return rt
