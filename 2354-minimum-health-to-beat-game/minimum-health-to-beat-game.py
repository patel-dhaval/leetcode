class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = 0
        total_damage = 0

        for d in damage:
            total_damage += d
            max_damage = max(max_damage, d)

        return total_damage - min(max_damage, armor) + 1
