class Troll:
    type_troll = "Normal"

    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points", 50)
        self.mana = kwargs.get("mana", 290)
        self.experience = kwargs.get("experience", 20)
        self.loot = kwargs.get(
            "loot", ["gold coins", "hand axes", "leather boots", "leather helmets", "meat"])

    def __str__(self):
        return "{} Troll, tiene {} puntos de vida y {} puntos de mana. Cuando lo matas otorga {} puntos de experiencia y estos objetos {}.\n{}".format(self.type_troll, self.hit_points, self.mana, self.experience, self.loot, self.atacar())

    def atacar(self):
        return "Te ataca y te baja 5 de HP"


class FrostTroll(Troll):
    type_troll = "Frost"

    def atacar(self):
        return "Te ataca y logra congelarte, te inmoviliza 2 segundos y te baja 10 HP"
