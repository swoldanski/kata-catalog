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
