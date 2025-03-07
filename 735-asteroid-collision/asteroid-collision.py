class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sim = []
        
        for asteroid in asteroids:
            # If asteroid is positive or the stack is empty, we just add it
            if not sim or asteroid > 0:
                sim.append(asteroid)
            elif asteroid < 0:
                # Handle collision with asteroids going to the right
                while sim and sim[-1] > 0 and sim[-1] < abs(asteroid):
                    sim.pop()
                
                # If both asteroids destroy each other
                if sim and sim[-1] == abs(asteroid):
                    sim.pop()
                # If current asteroid survives
                elif not sim or sim[-1] < 0:
                    sim.append(asteroid)
        
        return sim