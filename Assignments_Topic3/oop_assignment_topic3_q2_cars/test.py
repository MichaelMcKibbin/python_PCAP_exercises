from toyota_yaris import ToyotaYaris
from renault_twizy import RenaultTwizy

toyota_yaris = ToyotaYaris('Toyota','Yaris','192MC355','2019')
print(toyota_yaris)
print(toyota_yaris.refuel())
print(toyota_yaris.start_piston_engine())
print(toyota_yaris.accelerate())
print(toyota_yaris.brake())
print(toyota_yaris.turn_on_radio())

print()

renault_twizy = RenaultTwizy('Renault','Twizy','201EC415','2020')
print(renault_twizy)
print(renault_twizy.recharge())
print(renault_twizy.start_e_motor())
print(renault_twizy.accelerate())
print(renault_twizy.brake())
print(renault_twizy.turn_on_radio())