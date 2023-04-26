from abc import ABC, abstractmethod
class Transport(ABC):
    engine= str
    model= str
    millage =int
    color = str
    year = int
    max_speed=int
    def __init__(self, engine, model, millage, color, year, max_speed):
        self.engine = engine
        self.model = model
        self.millage = millage
        self.color=color
        self.year =year
        self. max_speed = max_speed
    @abstractmethod
    def start(self):
        print("start")

    @abstractmethod
    def stop(self):
        print("stop")

class AirTransport(Transport):
    place =int
    max_height = int
    wing_number = int
    def __init__(self, engine, model, millage, color, year, max_speed, place,max_height,wing_number):
        super().__init__(engine, model, millage, color, year, max_speed)
        self.place = place
        self.max_height=max_height
        self.wing_number=wing_number
    def fly(self):
        print(f" {self.model} может подниматься до {self.max_height} метров")

    def start(self):
        super().start()
        print("start")

    def stop(self):
        super().stop()
        print("stop")

class GroundTransport(Transport):
    taxi=bool
    def __init__(self,engine, model, millage, color, year, max_speed,taxi):
        super().__init__(engine, model, millage, color, year, max_speed)
        self.taxi=taxi
    def become_taxi(self):
        self.taxi=True

    def start(self):
        super().start()
        print('start')

    def stop(self):
        super().stop()
        print("stop")

class WaterTransport(Transport):
    def __init__(self, engine, model, millage, color, year, max_speed):
        super().__init__(engine, model, millage, color, year, max_speed)

    def start(self):
        super().start()
        print("start")

    def stop(self):
        super().stop()
        print("stop")
    def boat(self):
        print("Я могу плыть")
    def go_down(self):
        print("Я могу опуститься на дно")
    def go_up(self):
        print("Я могу всплывать")

class Airplane(AirTransport):
    wing_number = int
    pilot=str
    team=int
    def __init__(self,engine, model, millage, color, year, max_speed, place,max_height,wing_number,pilot,team):
        super().__init__(engine, model, millage, color, year, max_speed, place,max_height,wing_number)
        self.pilot=pilot
        self.team=team
class Car(GroundTransport):
    def __init__(self,engine, model, millage, color, year, max_speed,taxi,type_engine,type_gear):
        super().__init__(engine, model, millage, color, year, max_speed,taxi)
        self.type_engine=type_engine
        self.type_gear=type_gear

class Boat(WaterTransport):
    captain=str
    def __init__(self,engine, model, millage, color, year, max_speed,captain):
        super().__init__(engine, model, millage, color, year, max_speed)
        self.captain=captain
airplane=Airplane('class A',"Boeing",234,"red",1999, 1200, 600,12000,4,"Sergey",3)
car = Car(engine ="16 cylinder", model="Bentley", millage = 24000, color= "white", year = 2020, max_speed = 340,taxi =False,type_engine="Turbo",type_gear="Auto")
boat = Boat(engine ="class B", model="yacht", millage= 3000, color="black", year=1987, max_speed=230,captain="Ira")

print(airplane)
print(car)
print(boat)
print(Airplane.mro())
print(Car.mro())
print(Boat.mro())