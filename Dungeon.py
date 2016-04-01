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
            raise DungeonLevelError('Tile coordinate out of bounds: ({}, {})'.format(x, y))
        return False
    
    def make_grid(self, numRows, numCols):
        '''Warning: overwrites current grid'''
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
        
        try:
            return self.tile_at(neighborX, neighborY)
        except DungeonLevelError:
            raise DungeonLevelError('No valid neighbor in direction {}'.format(direction))
        return False


class DungeonLevelError(Exception):
    def __init__(self, message):
        super(DungeonLevelError, self).__init__(message)
    
    
class Tile(object):
    TILE_TYPES = ['floor', 'wall']
    def __init__(self, x, y, tileType='floor', isPassable=True):
        self.x = x
        self.y = y

        if tileType in self.TILE_TYPES:
            self.tileType = tileType
        else:
            raise ValueError('Invalid tile type: {}'.format(tileType))
        self.isPassable = isPassable
        
        self.items = []
        self.mobs = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.get_x, self.get_y)

    def get_tile_type(self):
        return self.tileType

    def get_is_passable(self):
        return self.isPassable
    
    def add_mob(self, mob):
        self.mobs.append(mob)
        return True
    
    def remove_mob(self, mob):
        try:
            self.mobs.remove(mob)
            return True
        except ValueError:
            raise TileError('Tile does not contain mob {}'.format(mob))
        return False
    
    def add_item(self, item):
        self.items.append(item)
        return True
    
    def remove_item(self, item):
        try:
            self.items.remove(item)
            return True
        except ValueError:
            raise TileError('Tile does not contain item {}'.format(item))
        return False


    class TileError(Exception):
        def __init__(self, message):
            super(DungeonLevelError, self).__init__(message)
 