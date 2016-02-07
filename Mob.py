class Mob:
    def __init__(self):
        pass

class Hero(Mob):
    HERO_SEXES = ('female', 'male')
    HERO_ROLES = ('archeologist', 'barbarian', 'caveperson', 'healer', 'knight', 'monk',
                  'priest', 'ranger', 'rogue', 'samurai', 'tourist', 'valkyrie', 'wizard')
    HERO_RACES = ('human', 'elf', 'dwarf', 'gnome', 'orc')
    HERO_ALIGNMENTS = ('lawful', 'neutral', 'chaotic')
    
    def __init__(self, name, sex, role, race, alignment):
        self.name = name
        
        sex = sex.lower()
        if (sex in HERO_SEXES):
            self.sex = sex
        else:
            raise ValueError('Invalid sex: {}'.format(sex))
        
        role = role.lower()
        if (role in HERO_ROLES:
            self.role = role
        else:
            raise ValueError('Invalid role: {}'.format(role))
        
        race = race.lower()
        if (race in HERO_RACES):
            self.race = race
        else:
            raise ValueError('Invalid race: {}'.format(race))
        
        alignment = alignment.lower()
        if (alignment in HERO_ALIGNMENTS):
            self.alignment = alignment
        else:
            raise ValueError('Invalid alignment: {}'.format(alignment))

        self.level = 1
        self.HP = 100

class Monster(Mob):
    def __init__(self):
        pass
