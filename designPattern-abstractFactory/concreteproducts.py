from abstractproducts import Lance, Sword

class Katana(Sword):
    def __init__(self):
        self.bladeType = "KATANA: Curved, Single cutting edge"

class Naginata(Lance):
    def __init__(self):
        self.bladeType = "NAGINATA: Curved, Not meant for stabbing"

class Gladius(Sword):
    def __init__(self):
        self.bladeType = "GLADIUS: Straight edge, Machete like"

class Pilum(Lance):
    def __init__(self):
        self.bladeType = "PILUM: Straight spike, For throwing and piercing"