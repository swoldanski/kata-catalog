class Character():
    """RPG character"""

    def __init__(self, name) -> None:
        """
        All Characters, when created, have:
            - Health, starting at 1000
            - Level, starting at 1
            - May be Alive or Dead, starting Alive (Alive may be a true/false)
        """
        self.name = name
        self.health = 1000
        self.level = 1
        self.alive = True

    def receive_damage(self, damage=0) -> None:
        """
        Characters can Deal Damage to Characters.
            - Damage is subtracted from Health
            - When damage received exceeds current Health, Health becomes 0 and the character dies
        """
        self.health = max(0, self.health-(damage))
        if self.health == 0:
            self.alive = False

    def receive_health(self, health=0) -> None:
        """
        A Character can Heal a Character.
            - Dead characters cannot be healed
            - Healing cannot raise health above 1000
        """
        if self.alive == True:
            self.health = min(1000, self.health+abs(health))

    def __repr__(self) -> str:
        return f"Character(name={self.name}, health={self.health}, level={self.level}, alive={self.alive})"
