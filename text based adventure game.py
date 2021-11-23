name=input("What is your name: ")
isCorrect=input("Your name is 'Rainbow Unicorn', is this correct y(yes) or n(no): ")
if isCorrect=='y':
    name="Rainbow Unicorn"
elif isCorrect =='n':
    print("Just kidding, your name is:", name, "\n")
else:
    pass

isDead=False
enemy_hp = 20

def death(reason):
    print("You died because", reason)
    return

def threeDoors():
    print('')
    choice=input("What door do you want to go in: ")
    while choice not in ("1", "2", "3"):
        choice = input("Input a valid choice ")
    if choice=="1":
        print("You find a treasure chest, congratulations")
    elif choice=="2":
        death("Instant Death")
    elif choice=="3":
        pass

playerStats={"Health":20}

while isDead==False:
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


    print("Enemy HP:", enemy_hp)

    if user_input == "sword" or user_input == "bow":
        user_input = input("Do you want to attack the enemy y(yes) or n(no): ")
        if user_input == "y":
            enemy_hp -= 20
        else:
            playerStats["Health"] -= 10
            print("You take 10 damage, your health is now", playerStats["Health"], "\n")
        print("Enemy HP:", enemy_hp)

    if playerStats["Health"] == 0:
        reason="Enemy killed you"
        death(reason)
        isDead=True

    if enemy_hp<=0:
        print("You killed the enemy")
        threeDoors()



print("END")
