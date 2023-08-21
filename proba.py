import os

class Car():

    n_sold = 0

    def __init__(self, make, model, price, tank, potrosnja=5, broj_putnika=4 ):
        self.make = make 
        self.model = model 
        self.price = price
        self.potrosnja = potrosnja 
        self.tank = tank
        self._current_fuel = tank
        self.mileage = 0


        Car.n_sold += 1

    @property
    def current_fuel(self):
        return self._current_fuel

    '''@current_fuel.setter
    def current_fuel(self, new_level):
        if new_level > self.tank or new_level < 0:
            raise Exception('Invalid fuel level')
        else:
            self._current_fuel = new_level'''

    


    def drive(self, distance):
        fuel_loss = distance / 100 * self.potrosnja 
        print('The trip was pleasnt')
        self.mileage += distance
        self.current_fuel -= fuel_loss

    def fill_gas(self, fuel_amount):
        self.current_fuel += fuel_amount


c = Car('mazda', 'mx5', 1800, 40)

dummy = c.current_fuel
print(dummy)
#c.current_fuel = x
#c.current_fuel.setter(c,x)


#c.current_fuel
#c.current_fuel()


