class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        return car

class Wheel:
    size = None

class Body:
    shape = None

class Engine:
    horsepower = None

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def setBody(self, body):
        self.__body = body

    def __str__(self):
        print("body : %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d" % self.__wheels[0].size)

class Builder:
    def getWheels(self): pass
    def getEngine(self): pass
    def getBody(self): pass

class JeepBuilder(Builder):

    def getWheels(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 5
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

if __name__ == "__main__" :

    jeepBuilder = JeepBuilder()

    director = Director()
    director.setBuilder(jeepBuilder)

    jeep = director.getCar()
    jeep.__str__()






































