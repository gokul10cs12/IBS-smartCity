class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("The dog {} has the age {}".format(self.name, self.age))


class Pug(Dog):
    def runs(self):
        print("{} runs slowly".format(self.name))


class Gsd(Dog):
    def runs(self):
        print("{} runs better than pug".format(self.name))


if __name__ == '__main__':
    pug = Pug("pug", 14)
    pug.details()
    pug.runs()
    print("pug sss",pug.name)

    gsd = Gsd("German Shepard", 3)
    gsd.details()
    gsd.runs()
