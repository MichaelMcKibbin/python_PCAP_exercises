from radio import Radio

class Car:

 def __init__(self, manufacturer, model, car_reg, year):
   self._manufacturer = manufacturer
   self._model = model
   self._car_registration = car_reg
   self._year = year
   self._radio = Radio()
   
 def get_manufacturer(self):
   return self._manufacturer
   
 def get_model(self):
   return self._model 
   
 def get_car_registration(self):
   return self._car_registration
   
 def get_year(self):
   return self._year 
   
 def turn_on_radio(self):
   return self._radio.turn_on()

 def accelerate(self):
   return 'Accelerate...'
 
 def brake(self):
   return 'Brake...'
   
 def __str__(self):
   return 'Manufacturer: ' + self._manufacturer + " - " + 'Model: ' + self._model + ' - ' + 'Car Registration: ' + self._car_registration + ' - ' + 'Year: ' + self._year
