class Dungeon(object):
    def __init__(self):
        self.dLevels = [] # bidirectional linked list
    
    def add_level(self, dLevel):
        self.dLevels.append(dLevel)
    

class DungeonLevel(object):
    def __init__(self):
        self.tileGrid = []
        maxX = -1
        maxY = -1
    
    def tile_at(self, x, y):
        try:
            return self.tileGrid[x][y]
        except IndexError:
            return False
    
    def make_grid(self, numRows, numCols):
        '''Replaces current grid with an empty one'''
        self.tileGrid = []
        self.maxX = numRows - 1
        self.maxY = numCols - 1
        for x in range(numRows):
            self.tileGrid.append([])
            for y in range(numCols):
                self.tileGrid[-1].append(Tile(x, y))
        return True
    
    def get_neighbor(self, tile, direction):
        direction = direction.lower()
        if direction not in ('n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'):
            raise ValueError('Invalid direction: {}'.format(direction))
        
        if 'e' in direction:
            neighborX = tile.x + 1
        elif 'w' in direction:
            neighborX = tile.x - 1
        else:
            neighborX = tile.x
        if 's' in direction:
            neighborY = tile.y + 1
        elif 'n' in direction:
            neighborY = tile.y - 1
        else:
            neighborY = tile.y
        
        if (neighborX >= 0 and neighborX <= self.maxX
                and neighborY >= 0 and neighborY <= self.maxY):
            return self.tile_at(neighborX, neighborY)
        else:
            return False
    
    
class Tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.items = []
        self.mobs = []
    
    def add_mob(self, mob):
        self.mobs.append(mob)
        return True
    
    def remove_mob(self, mob):
        self.mobs.remove(mob)
        return True
    
    def add_item(self, item):
        self.items.append(item)
        return True
    
    def remove_item(self, item):
        self.items.remove(item)
        return True
 