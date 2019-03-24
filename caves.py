# python 3.7

import random


def display_status():

    print()
    print('Gold: ' + str(gold))
    print('Health: ' + str(health))
    print('Turn: ' + str(game_turn))


def display_summary():

    print()
    print('### SUMMARY ###')
    print('Gold: ' + str(gold))
    print('Turns: ' + str(game_turn))
    print('Monsters: ' + str(monster_kills))


def select_cave():

    cave = ''

    while cave != '1' and cave != '2':
        cave = input('Select cave, 1 or 2: ')
    return cave


def add_gold():

    global gold

    gold_added = random.randint(0, 10)
    if gold_added > 0:
        gold += gold_added
        print(str(gold_added) + " gold added")


def add_health():

    global health

    if health == maxHealth:
        return

    if random.random() < 0.75:
        return

    health_added = min(random.randint(0, 10), maxHealth - health)
    if health_added > 0:
        health += health_added
        print('Health restored on ' + str(health_added))


def event_cave(cave_number):

    global health
    global strength
    global monster_kills
    player_lived = True

    cave_event = random.randint(1, 2)
    if cave_number == str(cave_event):
        add_gold()
    else:
        print('You meet monster')
        health -= random.randint(1, 10)
        player_lived = health > 0
        if player_lived:
            if random.random() < strength / maxStrength:   # kill monster
                print('You kill monster')
                monster_kills += 1
                add_gold()
                if strength < maxStrength:
                    strength += 0.1
            # health_event
            add_health()

    return player_lived


# game
maxHealth = 100
maxStrength = 10
gold = 0
health = maxHealth
strength = 1
game_turn = 1
monster_kills = 0

display_status()
currentCave = select_cave()
while event_cave(currentCave):
    game_turn += 1
    display_status()
    currentCave = select_cave()
display_summary()
