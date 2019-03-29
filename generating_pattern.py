import sys
import math
import abc
import copy




def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        else:
            print("You cant create 2 equal superheroes")
            raise IOError
        return instances[class_]
    return getinstance







class Union:
    fortune = 0
    is_alive = False
    is_active = False  ## is on smth field <=> location != -1
    healthpoint = 0  ## hp
    damage = 0
    energy = 0 ## how much activityes can do
    location = -1 ## number of field



class Hero(Union):
    def __init__(self):
        health = float('inf')
        self.energy = 2
        is_alive = True





class usual_voin(Union):
    "обычный солдат"
    def __init__(self, armor=0, weapon=0, shoes = 0):
        self.helthpoint = 10 + weapon
        self.fortune = 2 + shoes
        self.damage = 2 + armor
        self.energy = float('inf')
        is_alive = True




class Horse_voin(Union):
    def __init__(self):
        super().__init__()
        self.healthpoint -= 1.5
        self.fortune += 1.5



class Centaur(Horse_voin):
    def __init__(self):
        super().__init__()
        self.healthpoint += 1.5
        self.damage -= 1.5


class Horseman(Horse_voin):
    def __init__(self):
        super().__init__()
        self.healthpoint += 1
        self.fortune -= 1



class Bird(Union):
    def __init__(self):
        super().__init__()
        self.healthpoint -= 1.5
        self.fortune += 1.5



class aerobus(Bird):
    def __init__(self):
        super().__init__()
        self.healthpoint += 1.5
        self.damage -= 1.5



class FantasticBird(Bird):
    def __init__(self):
        super().__init__()
        self.fortune -= 1.5
        self.damage += 1.5




class Elf(usual_voin):
    def __init__(self):
        super().__init__()
        self.damage -= 1
        self.fortune += 1



class Human(usual_voin):
    def __init__(self):
        super().__init__()
        self.damage += 1
        self.fortune -= 5



class AbstractFactory(object):
    @abc.abstractmethod
    def create_usual_voin(self):
        pass

    @abc.abstractmethod
    def create_Horceman(self):
        pass

    @abc.abstractmethod
    def create_fantasticbird(self):
        pass

    @abc.abstractmethod
    def create_superhero(self, name):
        pass




class HumanFactory(AbstractFactory):

    def create_usual_voin(self):
        return Human()

    def create_bird(self):
        return aerobus()

    def create_horce_voin(self):
        return Horseman()


    def create_superhero(self, name):
        if (name == "MetalMen"):
            return MetalMen()
        if (name == "Joan of Arc"):
            return Joan_of_arc()
        if (name == "Invisible"):
            return Invisible()
        print("You cannot create this superhero")
        raise IOError



class FantacyFactory(AbstractFactory):

    def create_usual_voin(self):
        return Elf()

    def create_bird(self):
        return FantasticBird()

    def create_horce_voin(self):
        return Centaur()


    def create_superhero(self, name):
        if (name == "Halk"):
            return Halk()
        if (name == "Gandalf"):
            return Gandalf()
        if (name == "Frodo"):
            return Frodo()
        print("You cannot create this superhero")
        raise IOError


@singleton
class Halk(Hero):
    "power"
    def action(self):
        pass


@singleton
class Frodo(Hero):
    "inconspicuous"
    def action(self):
        pass


@singleton
class Gandalf(Hero):
    "mag"
    def action(self):
        pass

@singleton
class MetalMen(Hero):
    "power"
    def action(self):
        pass



@singleton
class Invisible(Hero):
    "inconspicuous"
    def action(self):
        pass


@singleton
class Joan_of_arc(Hero):
    "mag"
    def action(self):
        pass



class Prototype(object):

    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj




class Builder_voin:
    def build_armor(self):
        print("    Select level of armor(add your health):\n 0 - 0 coins, 3 - 1 coin, 6 - 2 coins\n Press the selected number")
        while (1):
            try:
                user_var = int(input())
                ##money -= user_var
                return user_var * 3, user_var
            except ValueError:
                pass



    def build_shoes(self):
        print("    Select level of fast shoes(add your fortune):\n 0 - 0 coins, 2 - 1 coin, 4 - 2 coins\n Press the selected number")
        while (1):
            try:
                user_var = int(input())
                ##money -= user_var
                return user_var * 2, user_var
            except ValueError:
                pass


    def build_weapon(self):
        print("    Select level of weapon(add your damage):\n 0 - 0 coins, 1 - 1 coin, 2 - 2 coins\n Press the selected number")
        while (1):
            try:
                user_var = int(input())
                ##money -= user_var
                return user_var, user_var
            except ValueError:
                pass


    def create_voin(self):
        armor, one_price = self.build_armor()
        shoes, two_price = self.build_shoes()
        weapon, third_price = self.build_weapon()
        return usual_voin(armor, weapon, shoes), one_price + two_price + third_price


class Player:
    def __init__(self, factory):
        self.money = 500
        self.factory = factory
        self.active_army = []  ## arm in field
        self.passive_army = []  ## arm in reserve




class Game:
    one = Player(HumanFactory)
    two = Player(HumanFactory)
    def start(self):
        print("Choose fraction for Player1: 1 - For human, 2 - For Fantastic")
        factory = HumanFactory()
        while(True):
            type1 = input()
            if (type1 == "1"):
                factory = HumanFactory()
                break
            elif (type1 == "2"):
                factory = FantacyFactory()
                break
            else:
                print("You should write 1 or 2")
        self.one = Player(factory)

        print("Choose fraction for Player2: 1 - For human, 2 - For Fantastic")
        factory = HumanFactory()
        while (True):
            type2 = input()
            if (type2 == "1"):
                factory = HumanFactory()
                break
            elif (type2 == "2"):
                factory = FantacyFactory()
                break
            else:
                print("You should write 1 or 2")
        self.two = Player(factory)

    def make_army(self):
        print("Now 1st Player make his army. He should choose 20 voin. Please, print 20 numbers one by one in column 1 for usualman, 2 for horseman, 3 for flyobject(can fly)")
        num = 0
        while (num < 20):
            t = input()
            if (t != '1' and t != '2' and t != '3'):
                print("incorrect input")
            elif (t == '1'):
                num += 1
                self.one.passive_army.append(self.one.factory.create_usual_voin())
            elif (t == '2'):
                num += 1
                self.one.passive_army.append(self.one.factory.create_horce_voin())
            else:
                num += 1
                self.one.passive_army.append(self.one.factory.create_bird())

        print("1st Player choose mercenary. Please, choose need amount(print number). Price of one mercenary is 2 coins")
        n = 0
        while (1):
            try:
                n = int(input())
                break
            except ValueError:
                pass
        if (n > 0):
            self.one.money -= 2 * n
            print(self.one.money)
            builder = Builder_voin()
            first, price = builder.create_voin()
            self.one.money -= price
            print(self.one.money)
            self.one.passive_army.append(first)
            prototype = Prototype()
            prototype.register('first', first)
            for i in range(n - 1):
                owl = prototype.clone('first', {'name': str(i + 1) + 'mercery'})
                self.one.passive_army.append(owl)

        print("Choose your superhero:")
        if (isinstance(self.one.factory, FantacyFactory)):
            print("Halk, Gandalf or Frodo - choose from them and print name")
            f = True
            while (f):
                name = input()
                try:
                    self.one.passive_army.append(self.one.factory.create_superhero(name))
                    break
                except IOError:
                    f = True

        else:
            print("MetalMen, Joan of Arc or Invisible - choose from them and print name")
            f = True
            while (f):
                name = input()
                try:
                    self.one.passive_army.append(self.one.factory.create_superhero(name))
                    break
                except IOError:
                    f = True





        print("Now 2nd Player make his army. He should choose 20 voin. Please, print 20 numbers one by one in column 1 for usualman, 2 for horseman, 3 for flyobject(can fly)")
        num = 0
        while (num < 20):
            t = input()
            if (t != '1' and t != '2' and t != '3'):
                print("incorrect input")
            elif (t == '1'):
                num += 1
                self.two.passive_army.append(self.two.factory.create_usual_voin())
            elif (t == '2'):
                num += 1
                self.one.passive_army.append(self.two.factory.create_horce_voin())
            else:
                num += 1
                self.one.passive_army.append(self.two.factory.create_bird())


        print("2nd Player choose mercenary. Please, choose need amount(print number). Price of one mercenary is 2 coins")
        n = 0
        while (1):
            try:
                n = int(input())
                break
            except ValueError:
                pass
        if (n > 0):
            self.two.money -= n * 2
            builder = Builder_voin()
            first, price = builder.create_voin()
            self.two.money -= price
            self.two.passive_army.append(first)
            prototype = Prototype()
            prototype.register('first', first)
            for i in range(n - 1):
                owl = prototype.clone('first', {'name': str(i + 1) + 'mercery'})
                self.two.passive_army.append(owl)


        print("Choose your superhero:")
        if (isinstance(self.two.factory, FantacyFactory)):
            print("Halk, Gandalf or Frodo - choose from them and print name")
            f =  True
            while (f):
                name = input()
                try:
                    self.two.passive_army.append(self.two.factory.create_superhero(name))
                    break
                except IOError:
                    f = True

        else:
            print("MetalMen, Joan of Arc or Invisible - choose from them and print name")
            f = True
            while (f):
                name = input()
                try:
                    self.two.passive_army.append(self.two.factory.create_superhero(name))
                    break
                except IOError:
                    f = True


game = Game()
game.start()
game.make_army()
