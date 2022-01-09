class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for m in sorted(asteroids):
            if mass >= m:
                mass += m
            else:
                return False
        return True
