class Robot:
    population = 0

    # __name:私有变量
    # 只想在类或对象中使用，就应该以单下划线前缀

    def __init__(self, name):
        # 动态的。。。
        self.name = name
        print('(Initialize {0})'.format(self.name))
        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    # 这个__del__很特别，在del droid用到
    def __del__(self):

        print('{0} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(
                Robot.population))

    def sayHi(self):
        print('Greetings, my master call me {0}.'.format(self.name))

    # howMany 实际上是属于类而不是对象的方法。
    def howMany():
        """ count """
        print('We have {0:d} robots.'.format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
print("droid1.population", droid1.population)
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3P0')
print("droid2.population", droid2.population)
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
del droid1
del droid2
Robot.howMany()
