from models.character import Character

if __name__ == "__main__":
    print("RPG kata")

    print("Iteration 1")

    print("Create character")
    my_hero = Character("swoldanski")
    print(my_hero)

    print(f"Apply 500 damage to {my_hero}")
    my_hero.receive_damage(500)
    print(my_hero)

    print(f"Apply 200 health to {my_hero}")
    my_hero.receive_health(200)
    print(my_hero)

    print(f"Apply 800 damage to {my_hero}")
    my_hero.receive_damage(800)
    print(my_hero)

    print(f"Apply 200 health to {my_hero}")
    my_hero.receive_health(200)
    print(my_hero)

    print("Iteration 2")

    print("Create character")
    my_hero = Character("swoldanski")
    enemy = Character("enemy")
    print(my_hero, enemy)

    damage = 500
    print(f"Apply {damage} damage to {my_hero} by {my_hero}")
    my_hero.receive_damage(damage=damage, attacker=my_hero)
    print(my_hero)

    print(f"Apply {damage} damage to {my_hero} by {enemy}")
    my_hero.receive_damage(damage=damage, attacker=enemy)
    print(my_hero)

    health = 501
    print(f"Apply {health} health to {my_hero} by {enemy}")
    my_hero.receive_health(health=health, healer=enemy)
    print(my_hero)

    print(f"Apply {health} health to {my_hero} by {my_hero}")
    my_hero.receive_health(health=health, healer=my_hero)
    print(my_hero)

    damage = 100
    my_hero.level = 42
    for i in range(10):
        enemy.level *= 2
        print(f"Apply {damage} damage to {my_hero} by {enemy}")
        my_hero.receive_damage(damage=damage, attacker=enemy)
        print(my_hero)
