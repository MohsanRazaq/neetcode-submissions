from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)],
            reverse=True
        )
        
        fleets = 0
        slowest_time = 0.0
        
        for _, time in cars:
            if time > slowest_time:
                fleets += 1
                slowest_time = time
                
        return fleets