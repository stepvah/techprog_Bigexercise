import unittest
import generating_pattern as f

class TestUm(unittest.TestCase):
    def testUnion(self):
        this = f.Union()
        self.assertEqual(type(this), f.Union)
        self.assertEqual(this.fortune,0)
        self.assertEqual(this.is_alive, False)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 0)
        self.assertEqual(this.damage, 0)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)


    def testHero(self):
        this = f.Hero()
        self.assertEqual(type(this), f.Hero)
        self.assertEqual(this.fortune, 0)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, float('inf'))
        self.assertEqual(this.damage, 0)
        self.assertEqual(this.energy, 2)
        self.assertEqual(this.location, -1)


    def testUsual(self):
        this = f.usual_voin(1, 2, 3)
        self.assertEqual(type(this), f.usual_voin)
        self.assertEqual(this.fortune, 5)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 12)
        self.assertEqual(this.damage, 3)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)

    def testHorce_Voin(self):
        this = f.Horse_voin()
        self.assertEqual(type(this), f.Horse_voin)
        self.assertEqual(this.fortune, 3.5)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 7.5)
        self.assertEqual(this.damage, 2)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)

    def  testCentaur(self):
        this = f.Centaur()
        self.assertEqual(type(this), f.Centaur)
        self.assertEqual(this.fortune, 3.5)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 10)
        self.assertEqual(this.damage, 0.5)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)


    def testHorseman(self):
        this = f.Horseman()
        self.assertEqual(type(this), f.Horseman)
        self.assertEqual(this.fortune, 2.5)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 9.5)
        self.assertEqual(this.damage, 2)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)


    def testBird(self):
        this = f.Bird()
        self.assertEqual(type(this), f.Bird)
        self.assertEqual(this.fortune, 3.5)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 7.5)
        self.assertEqual(this.damage, 2)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)

    def testaerobus(self):
        this = f.aerobus()
        self.assertEqual(type(this), f.aerobus)
        self.assertEqual(this.fortune, 3.5)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 10)
        self.assertEqual(this.damage, 0.5)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)

    def testFantasticBird(self):
        this = f.FantasticBird()
        self.assertEqual(type(this), f.FantasticBird)
        self.assertEqual(this.fortune, 2)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 7.5)
        self.assertEqual(this.damage, 3.5)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)


    def testElf(self):
        this = f.Elf()
        self.assertEqual(type(this), f.Elf)
        self.assertEqual(this.fortune, 3)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 10)
        self.assertEqual(this.damage, 1)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)

    def testHuman(self):
        this = f.Human()
        self.assertEqual(type(this), f.Human)
        self.assertEqual(this.fortune, 2)
        self.assertEqual(this.is_alive, True)
        self.assertEqual(this.is_active, False)
        self.assertEqual(this.healthpoint, 5)
        self.assertEqual(this.damage, 3)
        self.assertEqual(this.energy, float('inf'))
        self.assertEqual(this.location, -1)

    def testABCFabric(self):
        this = f.AbstractFactory()
        self.assertEqual(type(this), f.AbstractFactory)
        self.assertEqual(this.create_usual_voin(), None)
        self.assertEqual(this.create_Horceman(), None)
        self.assertEqual(this.create_fantasticbird(), None)
        self.assertEqual(this.create_superhero("Halk"), None)

    def testHumanFactory(self):
        this = f.HumanFactory()
        self.assertEqual(type(this.create_usual_voin()), f.Human)
        self.assertEqual(type(this.create_bird()), f.aerobus)
        self.assertEqual(type(this.create_horce_voin()), f.Horseman)






if (__name__ == "__main__"):
    unittest.main()

