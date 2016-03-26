import Dungeon
import Mob
import Item

def main():
    # create dungeon with a single NxN level
    N = 3   # must be >= 2
    testDungeon = Dungeon.Dungeon()
    testLevel = Dungeon.DungeonLevel()
    testLevel.make_grid(N, N)
    testDungeon.add_level(testLevel)
    
    assert(len(testDungeon.dLevels) == 1)
    assert(testLevel.tile_at(testLevel.maxX, testLevel.maxY))
    assert(not testLevel.tile_at(N, 0))
    assert(testLevel.tile_at(0, 0) == testLevel.get_neighbor(testLevel.tile_at(1, 1), 'nw'))
    assert(not testLevel.get_neighbor(testLevel.tile_at(0, 0), 'n'))
    print 'Dungeon creation passed'
    
    # create hero and place at (1, 1)
    testHero = Mob.Hero('tester', 'female', 'archeologist', 'dwarf', 'chaotic')
    testHero.set_dungeon_level(testLevel)
    testHero.set_location(testLevel.tile_at(1, 1))
    assert(testHero.get_location().x == 1 and testHero.get_location().y == 1)
    print 'Hero creation passed'
    
    # place food ration at (1, 0) and have hero pick up
    testComestible = Item.FoodRation()
    testLevel.tile_at(1, 0).add_item(testComestible)
    assert(len(testLevel.tile_at(1, 0).items) == 1)
    testHero.move('n')
    assert(testHero.get_location() == testLevel.tile_at(1, 0))
    assert(len(testLevel.tile_at(1, 1).mobs) == 0)
    assert(testLevel.tile_at(1, 0).mobs[0] == testHero)
    testHero.pick_up(testComestible)
    assert(len(testLevel.tile_at(1, 0).items) == 0)
    assert(testHero.inventory[0] == testComestible)
    assert(testHero.get_weight_carried() == testComestible.get_weight())
    print 'Hero movement and pickup passed'

    # have hero eat food ration
    heroNutritionBefore = testHero.get_nutrition()
    testHero.eat(testComestible)
    heroNutritionAfter = testHero.get_nutrition()
    assert(len(testHero.inventory) == 0)
    assert(heroNutritionAfter - heroNutritionBefore == testComestible.get_nutrition_value())
    assert(testHero.get_weight_carried() == 0)
    print 'Hero eating passed'

    return testDungeon

if __name__ == "__main__":
    main()
