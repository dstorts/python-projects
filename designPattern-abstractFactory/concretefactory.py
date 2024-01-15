from blade import Blade
from concreteproducts import Katana, Naginata, Gladius, Pilum

class JapanBladeFactory(Blade):
    def create_lance(self):
        return Naginata()
    def create_sword(self):
        return Katana()

class RomanBladeFactory(Blade):
    def create_lance(self):
        return Pilum()
    def create_sword(self):
        return Gladius()