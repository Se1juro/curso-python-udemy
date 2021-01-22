import player
import troll
# sorcerer = Player(40,80,"Sorcerer","Rayo Hielo")
sorcerer = player.Sorcerer(hit_points=40, mana=80)
print(sorcerer)

knight = player.Knight(hit_points=80, mana=40)
print(knight)

paladin = player.Paladin(hit_points=60, mana=60)
print(paladin)

druida = player.Druida(hit_points=50, mana=70)
print(druida)

# Trolls

normal_troll = troll.Troll(hit_points=50, mana=290, experience=20, loot=[
    "gold coins", "hand axes", "leather boots", "leather helmets", "meat"])

print(normal_troll)
# print(normal_troll.atacar())

frost_Troll = troll.FrostTroll(hit_points=55, mana=300, experience=23, loot=[
                               "carry fish", "gold coins", "rapiers", "spears", "wooden shields"])
print(frost_Troll)
# print(frost_Troll.atacar())
