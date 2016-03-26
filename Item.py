class Item(object):
    def __init__(self):
        self.weight = 0

    def get_weight(self):
    	return self.weight 
    

class Weapon(Item):
    def __init__(self):
    	super(Weapon, self).__init__()


class Comestible(Item):
	def __init__(self):
		super(Comestible, self).__init__()
		self.nutritionValue = 0
		self.isRotten = False

	def get_nutrition_value(self):
		return self.nutritionValue


class FoodRation(Comestible):
	def __init__(self):
		super(FoodRation, self).__init__()
		self.weight = 20
		self.nutritionValue = 800

