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
        drawn_balls = []
        if draws >= length:
            drawn_balls.extend(self.contents)
            self.contents.clear()
            return drawn_balls        
        for i in range(draws):
            ball_to_draw = random.randint(0, length-i-1)
            drawn_balls.append(self.contents.pop(ball_to_draw))
        return drawn_balls

    def put_back(self, contents):
        for content in contents:
            self.contents.append(content)

    
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_exp = 0
    # returns list of the balls drawn from the hat
    for _ in range(num_experiments):
        hat_draw = hat.draw(num_balls_drawn)
        dict_balls = expected_balls.copy()
        for color in hat_draw:
            if color in dict_balls:
                dict_balls[color] -= 1
                if dict_balls[color] == 0:
                    del dict_balls[color]
                    if not dict_balls:
                        success_exp += 1
                        break
            else:
                continue
        hat.put_back(hat_draw)
    return success_exp/num_experiments

            

hat1 = Hat(black=6, red=4, green=3)
print(hat1.contents)
print(experiment(hat=hat1,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000))