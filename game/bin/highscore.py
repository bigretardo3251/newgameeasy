import json
class Highscore:
    def __init__(self,points):
        self.points = points
    def update(self):
        self.points += 100
    def read(self):
        return self.points
      
