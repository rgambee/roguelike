#import Dungeon

class Mob:
    def __init__(self):
        pass
    
    def set_dungeon_level(self, dLevel):
        self.dLevel = dLevel
    
    def set_location(self, tile):
        if self.get_location():
            self.get_location().remove_mob(self)
        self.location = tile
        tile.add_mob(self)
        return True
    
    def get_location(self):
        try:
            return self.location
        except AttributeError:
            return False
    
    def move(self, direction):
        currentLocation = self.get_location()
        if currentLocation:
            newLocation = self.dLevel.get_neighbor(self.get_location(), direction)
            if newLocation:
                return self.set_location(newLocation)
        return False
    
    def pick_up(self, item):
        self.get_location().remove_item(item)
        self.inventory.append(item)
        return True


class Hero(Mob):
    HERO_SEXES = ('female', 'male')
    HERO_ROLES = ('archeologist', 'barbarian', 'caveperson', 'healer', 'knight', 'monk',
                  'priest', 'ranger', 'rogue', 'samurai', 'tourist', 'valkyrie', 'wizard')
    HERO_RACES = ('dwarf', 'elf', 'gnome', 'human', 'orc')
    HERO_ALIGNMENTS = ('chaotic', 'lawful', 'neutral')
    
    def __init__(self, name, sex, role, race, alignment):
        self.name = name
        
        sex = sex.lower()
        if (sex in Hero.HERO_SEXES):
            self.sex = sex
        else:
            raise ValueError('Invalid sex: {}'.format(sex))
        
        role = role.lower()
        if (role in Hero.HERO_ROLES):
            self.role = role
        else:
            raise ValueError('Invalid role: {}'.format(role))
        
        race = race.lower()
        if (race in Hero.HERO_RACES):
            self.race = race
        else:
            raise ValueError('Invalid race: {}'.format(race))
        
        alignment = alignment.lower()
        if (alignment in Hero.HERO_ALIGNMENTS):
            self.alignment = alignment
        else:
            raise ValueError('Invalid alignment: {}'.format(alignment))

        self.health = 100
        self.maxHealth = 100
        self.power = 10
        self.maxPower = 10
        self.level = 1
        self.experience = 0
        self.gold = 0
        self.inventory = []


class Monster(Mob):
    def __init__(self):
        pass
