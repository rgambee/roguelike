class Mob:
    def __init__(self):
        pass

class Hero(Mob):
    def __init__(self, name, sex, role, alignment):
        self.name = name
        self.sex = sex
        self.role = role
        self.alignment = alignment

        self.level = 1
        self.HP = 100

class Monster(Mob):
    def __init__(self):
        pass
