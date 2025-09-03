import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []        
        for key, value in kwargs.items():
            while value>0:
                self.contents.append(key)
                value -= 1

    def draw(self, draws):
        length = len(self.contents)
        if draws > length:
            return self.contents
        contents_poppable = self.contents
        drawn_balls = []
        for i in range(draws):
            ball_to_draw = random.randint(0, length-i)
            drawn_balls.append(contents_poppable(ball_to_draw))
        return drawn_balls
    
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # returns list of the balls drawn from the hat
    hat.draw(num_balls_drawn)

hat1 = Hat(yellow=3, red=2)
print(hat1.contents)