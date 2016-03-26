class Item(object):
    def __init__(self):
        self.weight = 0

    def get_weight(self):
    	return self.weight 
    

class Weapon(Item):
    def __init__(self):
        pass
    

class Comestible(Item):
	def __init__(self):
		self.nutritionValue = 0
		self.isRotten = False

	def get_nutrition_value(self):
		return self.nutritionValue


class FoodRation(Comestible):
	def __init__(self):
		self.weight = 20
		self.nutritionValue = 800

