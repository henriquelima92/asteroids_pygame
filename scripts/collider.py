class Collider(object):
    def __init__(self, hitbox):
        self.hitbox = hitbox

    def check_collision(self, position, enemy):
        self.posiition = position

        if position.x < (enemy.position.x + enemy.scale.x) and (position.x + self.hitbox[2]) > enemy.position.x: 
            if position.y < (enemy.position.y + enemy.scale.y) and (position.y + self.hitbox[3]) > enemy.position.y:
                return True
        return False

