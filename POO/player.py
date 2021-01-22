class Player:
    vocation = "No Vocation"
    spell = "Puff"
    movement_speed = 50
    # Puedo pasar argumentos normalmente sin el kwargs

    def __init__(self, **kwargs):
        # self.hit_points=hit_points
        self.name = input("Elige tu nombre de usuario: ")
        self.hit_points = kwargs.get("hit_points", 50)
        self.mana = kwargs.get("mana", 50)

    def __str__(self):
        return "{} es un {} tiene: {} hit_points y {} mana, puede lanzar {} y corre {} movement_speed\n".format(
            self.name,
            self.vocation,
            self.hit_points,
            self.mana,
            self.castSpell(),
            self.movement_speed
        )

    # Todos los metodos en las clases llevan por lo menos un argumento, self, el cual hace referencia a la clase.
    def castSpell(self):
        return self.spell


class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Rayo de Hielo"
    movement_speed = "30"

    # De esta manera se sobreescribe un metodo
    def castSpell(self):
        return "{} y Respiro".format(self.spell)


class Knight(Player):
    vocation = "Knight"
    spell = "Danza Espada"
    movement_speed = "50"


class Druida(Player):
    vocation = "Druida"
    spell = "Gigadrenado"
    movement_speed = "30"

    def castSpell(self):
        return "{} y Respiro".format(self.spell)


class Paladin(Player):
    vocation = "Paladin"
    spell = "Flecha Fuego"
    movement_speed = "40"
