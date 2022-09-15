enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

#Global Scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

#There is no Block scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)