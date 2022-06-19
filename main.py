#Pokemon

import random as rd

class Pokemon:
    def __init__(self, name, type, lvl, stats, attacks):
        self._name = name
        self._type = type
        self._lvl = lvl
        self._stats = stats #diccionario
        self._attacks = attacks #diccionario de ataques
    def receive_damage(self, damage):
        return self._stats["Life"] - damage

class Type:
    def __init__(self, name, type_effectiveness, attacks):
        self._name = name
        self._type_effectiveness = type_effectiveness #diccionario de tipos
        self._attacks = attacks #diccionario de ataques



class Attack:
    def __init__(self, name, type, category, power):
        self._name = name
        self._type = type #objeto tipo
        self._category = category
        self._power = power

    def damage_calculator(self, pokemon_giving, pokemon_receiving):
        type = self._type
        if self._category == "Special":
            damage = ((2 * pokemon_giving._lvl / 5 + 2)*self._power * pokemon_giving._stats["Special Attack"] / pokemon_giving._stats["Special Defense"] / 50 + 2) * type._type_effectiveness[pokemon_receiving._type]
        else:
            damage = ((2 * pokemon_giving._lvl / 5 + 2) * self._power * pokemon_giving._stats["Attack"] / pokemon_giving._stats["Defense"] / 50 + 2) * type._type_effectiveness[pokemon_receiving._type]
        return damage


class Player:
    def __int__(self, pokemons):
        self._pokemons = pokemons #diccionario de pokemons

    def begin_battle(self, player2):
        battle(self, player2)


#def battle(player1, player2):
 #   any_pokemon_alive_p1 = False
    #any_pokemon_alive_p2 = False
    #for pokemon in player1._pokemons:
     #   if pokemon._stats["Life"] > 0:
      #      any_pokemon_alive_p1 = True
    #for pokemon in player2._pokemons:
     #   if pokemon._stats["Life"] > 0:
      #      any_pokemon_alive_p2 = True
    #while any_pokemon_alive_p1 and any_pokemon_alive_p2:
     #   chosen_pokemon_p1 = input("Pick a Pokemon, Player 1")
      #  chosen_pokemon_p2 = input("Pick a Pokemon, Player 2")
       # if chosen_pokemon_p1._stats["Speed"] > chosen_pokemon_p2._stats["Speed"]:
        #    first_pokemon = chosen_pokemon_p1
         #   second_pokemon = chosen_pokemon_p2
          #  chosen_attack_p1 = input("Pick an Attack, Player 1")
           # damage = chosen_attack_p1.damage_calculator(first_pokemon, second_pokemon)
            #chosen_pokemon_p2._stats["Life"] = chosen_pokemon_p2.receive_damage(damage)
        #else:
         #   first_pokemon = chosen_pokemon_p2
          #  chosen_attack_p2 = input("Pick an Attack, Player 2")

normal_effectiveness = {}
normal_attacks = {}

fire_effectiveness = {}
fire_attacks = {}

grass_effectiveness = {}
grass_attacks = {}

water_effectiveness = {}
water_attacks = {}

normal = Type("Normal", normal_effectiveness, normal_attacks)

fire = Type("Fire", fire_effectiveness, fire_attacks)

grass = Type("Grass", grass_effectiveness, grass_attacks)

water = Type("Water", water_effectiveness, water_attacks)



tackle = Attack("Tackle", normal, "Physical", 40)

ember = Attack("Ember", fire, "Special", 40)

razor_leaf = Attack("Razor Leaf", grass, "Physical", 45)

water_gun = Attack("Water Gun", water, "Especial", 40)


normal_effectiveness = {
    normal: 1,
    fire: 1,
    grass: 1,
    water: 1
}
normal._type_effectiveness = normal_effectiveness


fire_effectiveness = {
    normal: 1,
    fire: 1/2,
    grass: 2,
    water: 1/2
}
fire._type_effectiveness = fire_effectiveness

grass_effectiveness = {
    normal: 1,
    fire: 1/2,
    grass: 1/2,
    water: 2
}
grass._type_effectiveness = grass_effectiveness

water_effectiveness = {
    normal: 1,
    fire: 2,
    grass:1/2,
    water:1/2
}

normal_attacks = {
    "Tackle": tackle
}

fire_attacks = {
    "Ember": ember
}

grass_attacks = {
    "Razor Leaf": razor_leaf
}

water_attacks = {
    "Water Gun": water_gun
}

rattata_stats={
    "HP": 19,
    "Attack": 12,
    "Defense": 11,
    "Special Attack": 9,
    "Special Defense": 11,
    "Speed": 12
}
rattata_attacks = {
    "Tackle": tackle
}
rattata = Pokemon("Rattata", normal, 5, rattata_stats, rattata_attacks)

cyndaquil_stats = {
    "HP": 20,
    "Attack": 12,
    "Defense": 10,
    "Special Attack": 12,
    "Special Defense": 12,
    "Speed": 13
}
cyndaquil_attacks = {
    "Ember": ember
}
cyndaquil = Pokemon("Cyndaquil", fire, 5, cyndaquil_stats, cyndaquil_attacks)

chikorita_stats = {
    "HP": 19,
    "Attack": 12,
    "Defense": 10,
    "Special Attack": 9,
    "Special Defense": 10,
    "Speed": 12
}
chikorita_attacks = {
    "Razor Leaf": razor_leaf
}
chikorita = Pokemon("Chikorita", grass, 5, chikorita_stats, chikorita_stats)

totodile_stats={
    "HP": 21,
    "Attack": 13,
    "Defense": 10,
    "Special Attack": 10,
    "Special Defense": 12,
    "Speed": 10
}
totodile_attacks = {
    "Water Gun": water_gun
}
totodile = Pokemon("Totodile", water, 5, totodile_stats, totodile_attacks)

damage_razor_leaf = razor_leaf.damage_calculator(chikorita, totodile)

if __name__ == '__main__':
    print(int(damage_razor_leaf))