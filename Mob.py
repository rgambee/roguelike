import Dungeon
import Item

class Mob(object):
    def __init__(self):
        self.health = 100
        self.maxHealth = 100
        self.nutrition = 900
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.weightCarried = 0
        self.attributes = {'strength':1, 'dexterity':1, 'constitution':1,
                           'intelligence':1, 'wisdom':1, 'charisma':1}
    
    def set_dungeon_level(self, dLevel):
        self.dLevel = dLevel
        return True
    
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

    def add_to_inventory(self, item):
        self.inventory.append(item)
        return True

    def remove_from_inventory(self, item):
        try:
            self.inventory.remove(item)
            return True
        except:
            return False
    
    def pick_up(self, item):
        if self.get_location().remove_item(item):
            self.add_to_inventory(item)
            self.update_weight_carried()
            return True
        return False

    def eat(self, comestible):
        if isinstance(comestible, Item.Comestible):
            self.remove_from_inventory(comestible)
            self.add_nutrition(comestible.get_nutrition_value())
            self.update_weight_carried()
            return True
        return False

    def get_nutrition(self):
        return self.nutrition

    def add_nutrition(self, amount):
        '''amount can be negative (indicates loss of nutrition)'''
        self.nutrition += amount
        return True

    def get_weight_carried(self):
        return self.weightCarried

    def update_weight_carried(self):
        w = 0
        for i in self.inventory:
            w += i.get_weight()
        self.weightCarried = w
        return True

    def add_experience(self, amount):
        '''amount can be negative (indicates loss of experience)'''
        self.experience += amount
        return True


class Hero(Mob):
    HERO_SEXES = ('female', 'male')
    HERO_ROLES = ('archeologist', 'barbarian', 'caveperson', 'healer', 'knight', 'monk',
                  'priest', 'ranger', 'rogue', 'samurai', 'tourist', 'valkyrie', 'wizard')
    HERO_RACES = ('dwarf', 'elf', 'gnome', 'human', 'orc')
    HERO_ALIGNMENTS = ('chaotic', 'lawful', 'neutral')
    
    def __init__(self, name, sex, role, race, alignment):
        super(Hero, self).__init__()

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

        self.power = 10
        self.maxPower = 10
        self.gold = 0


class Monster(Mob):
    def __init__(self):
        pass
