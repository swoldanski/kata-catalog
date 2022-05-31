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

    def receive_damage(self, damage=0, attacker=None) -> None:
        """
        Characters can Deal Damage to Characters.
            - Damage is subtracted from Health
            - When damage received exceeds current Health, Health becomes 0 and the character dies

        A Character cannot Deal Damage to itself.

        When dealing damage:
            - If the target is 5 or more Levels above the attacker, Damage is reduced by 50%
            - If the target is 5 or more Levels below the attacker, Damage is increased by 50%
        """
        if attacker is self:
            return
        if attacker:
            damage = self.damage_calculator(damage=damage, attacker=attacker)
        self.health = max(0, self.health-(damage))
        if self.health == 0:
            self.alive = False

    def damage_calculator(self, damage=0, attacker=None):
        """
        When dealing damage:
            - If the target is 5 or more Levels above the attacker, Damage is reduced by 50%
            - If the target is 5 or more Levels below the attacker, Damage is increased by 50%
        """
        level_difference = abs(attacker.level - self.level)
        if level_difference < 5:
            return damage

        if attacker.level < self.level:
            return damage // 2

        return int(damage * 1.5)

    def receive_health(self, health=0, healer=None) -> None:
        """
        A Character can Heal a Character.
            - Dead characters cannot be healed
            - Healing cannot raise health above 1000

        A Character can only Heal itself.
        """
        if healer and healer is not self:
            return
        if self.alive == True:
            self.health = min(1000, self.health+abs(health))

    def __repr__(self) -> str:
        return f"Character(name={self.name}, health={self.health}, level={self.level}, alive={self.alive})"
