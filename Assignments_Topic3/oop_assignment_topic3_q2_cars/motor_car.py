from car import Car
from piston_engine import PistonEngine

class MotorCar(Car):
 
 def __init__(self, manufacturer, model, car_reg, year):
  super().__init__(manufacturer, model, car_reg, year)
  self._piston_engine = PistonEngine()
  
 def refuel(self):
  return 'Refuelling a motor car.'
  
 def start_piston_engine(self):
  return self._piston_engine.start()
 
 