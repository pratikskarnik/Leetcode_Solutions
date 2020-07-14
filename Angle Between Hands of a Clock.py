class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour=hour%12
        hourangle=hour*30
        minangle=minutes*6
        hourangle+=minutes*0.5
        return min(abs(hourangle-minangle), 360-abs(minangle-hourangle))

