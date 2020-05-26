import random

class Auto:
    list_auto = ['renault', 'pegeout', 'ZAZ']

    def __init__(self, name, **kwargs):
        self.name = name

    # Make new instance attributes 
        for attribute, value in kwargs.items():
            #print(f"{key} = {value}")
            #setattr(self, attribute, value)
            self.__dict__.update(kwargs)
    
    def randomnum(self):
        print("called by {}".format(self))
        return bool(random.randint(0, 1))

    def call_auto(self):
        for auto in self.list_auto:
            print(auto)

    def make_dict(self, **kwargs):
        print(type(kwargs))
        for key, value in kwargs.items():
            print(f"{key} = {value}")

    def make_tuple_list(self, *args):
        print(type(args))
        args = list(args)
        print(type(args))
        
class RaceCar:
    def __init__(self, color, fuel_remaining, **kwargs):
        laps = 0
        self.color = color
        self.fuel_remaining = fuel_remaining
        for attr, value in kwargs.items():
            setattr(self, attr, value)
            
    def run_lap(self, length):
        self.fuel_remaining -= (length * 0.125)
        self.laps += 1
        