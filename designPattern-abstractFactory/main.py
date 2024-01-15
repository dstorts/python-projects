# This is a demonstration of the abstract factory pattern in python
from concretefactory import JapanBladeFactory, RomanBladeFactory

JapaneseBladeFactory = JapanBladeFactory()
RomanBladeFactory = RomanBladeFactory()

katana = JapaneseBladeFactory.create_sword()
naginata = JapaneseBladeFactory.create_lance()

gladius = RomanBladeFactory.create_sword()
pilum = RomanBladeFactory.create_lance()


print("Time to forge some weapons!")
print(katana.Description())
print(naginata.Description())
print(gladius.Description())
print(pilum.Description())
