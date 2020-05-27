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
        self.laps = 0
        self.color = str(color)
        self.fuel_remaining = fuel_remaining
        for attr, value in kwargs.items():
            setattr(self, attr, value)
    
    def __str__(self):
        return f"Instance class: {self.__class__.__name__}"

    def __add__(self, color_code):
        return self.color + str(color_code)
            
    def run_lap(self, length):
        self.fuel_remaining -= (length * 0.125)
        self.laps += 1

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __str__(self):
        output = []
        for blip in self.pattern:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)
    

class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)
         
    
    
