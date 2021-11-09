print("OH NOO! I AM BEING ATTACKED!")
print("You have encountered an enemy!")
print()
inventory = ['potion', 'shield', 'sword', 'bow']
print(inventory)
user_input = input("Pick an item from the inventory: ")
if user_input in inventory:
  if user_input == "sword":
    print("You have a sword!")
  elif user_input == "potion":
    print("You have selected a potion.")
  elif user_input == "bow":
    print("You have a bow!")
  elif user_input == "shield":
    print("You have a shield.")
else:
    print("The item you have selected is not in the inventory. Pick another item.")

enemy_hp = 20
print("Enemy HP:", enemy_hp)

if user_input == "sword" or user_input == "bow":
    user_input = input("Do you want to attack the enemy y(yes) or n(no): ")
    if user_input == "y":
        enemy_hp -= 10
    else:
        enemy_hp = enemy_hp
    print("Enemy HP:", enemy_hp)
