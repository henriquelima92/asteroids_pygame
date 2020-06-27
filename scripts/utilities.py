class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_vector2(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_vector2(self):
        return [self.x, self.y]

class Collider(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_position(self, x,y):
        self.x = x
        self.y = y

    def check_collision(self, obj):
        diffx = self.x - obj.x
        diffy = self.y - obj.y
        if diffx < self.size.x and diffx > (self.size.x * -1):
            if diffy < self.size.y and diffx > (self.size.y * -1):
                return True
        return False

