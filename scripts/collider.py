class Collider(object):
    def __init__(self, position, scale):
        self.position = position
        self.scale = scale

    def check_collision(self, position, enemy):
        self.posiition = position

        if self.position.x < enemy.position.x + enemy.scale.x and self.position.x + self.scale.x > enemy.position.x and self.position.y < enemy.position.y + enemy.scale.y and self.position.y + self.scale.y > enemy.position.y:
            return True
        return False

