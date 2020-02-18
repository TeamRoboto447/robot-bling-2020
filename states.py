
class idle:
    def __init__(self,dictOfGroups,tables,pixels):
        self.dic = dictOfGroups
        self.tables = tables
        self.pixels = pixels
    def start(self):
        color = {"red":(255,0,0),"blue":(0,0,255)}[self.tables.getTeamColor()]
        self.dic["chassis"].fill(color)
        self.dic["turret"].fill(color)
        self.pixels.show()
    def run(self):
        pass
    def end(self):
        
