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