class Dungeon:
    def __init__(self):
        self.dlevels = []
    

class DungeonLevel:
    def __init__(self):
        pass
    
    
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.items = []
        self.mobs = []

