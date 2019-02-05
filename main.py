from Day6 import Person

print("This is the instuction......")
player = Person("Daniel",500, 100, 50)
enemy = Person("Vampire",1000,100,20)

player.stats()
enemy.stats()
running = True
while running:
    print(player.name)
    print("Choose your action: ")
    player.choose_action()
    choice = int(input(">>>: "))
    action_index = choice - 1
    if action_index == 0:
        demage = player.generate_atk_damage()
        enemy.take_damage(demage)
        print("You attacked{} and deal {} demage".format(enemy.name, demage))
    else:
        print("Choose a correct number ")
        continue

    #Enemy"s Turn
    enemy_choice = 0
    if enemy_choice == 0:
        enemy_damage = enemy.generate_atk_damage()
        player.take_damage(enemy_damage)
        print("{} attacked and {} damage".format(enemy.name, 3))
        #print("{} attacked and {} damage".format(enemy.name, enemy.damage))


    player.stats()
    enemy.stats()
    if player.hp == 0:
        print("You lost")
        runing = False
    elif enemy.hp == 0:
        print("You won")
        runing = False
