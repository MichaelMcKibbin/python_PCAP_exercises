from car import Car
from electric_motor import ElectricMotor

class ElectricCar(Car):
 
  def __init__(self, manufacturer, model, car_reg, year):
    super().__init__(manufacturer, model, car_reg, year)
    self._electric_motor = ElectricMotor()
    
  def recharge(self):
    return 'Recharging an electric car.'
    
  def start_e_motor(self):
    return self._electric_motor.start()