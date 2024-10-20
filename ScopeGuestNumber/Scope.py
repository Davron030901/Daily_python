# enemies=1
#
# def increase_enimies():
#     enemies=2
#     print(f" enimies inside function: {enemies}")
# increase_enimies()
# print(f" enimies inside function: {enemies}")
#
# def drink_potion():
#     potion_strength=2
#     print(potion_strength)
# drink_potion()
# player_health=10
# def game():
#     def drink_potion():
#         potion_strenth=2
#         print(player_health)
#     drink_potion()
# game()
# There is no Block Scope
#Modifying Global Scope

enemies=1
def increase_enemies():
    print(enemies)
increase_enemies()
print(enemies)
