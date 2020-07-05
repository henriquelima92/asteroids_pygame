class Highscore(object):

    def __init__(self):
        self.current_points = 0
    
    def increase_points(self, asteroid_type):
        if asteroid_type == 1:
            self.current_points += 1
        elif asteroid_type == 2:
            self.current_points += 2
        elif asteroid_type == 3:
            self.current_points += 3
        elif asteroid_type == 4:
            self.current_points += 4