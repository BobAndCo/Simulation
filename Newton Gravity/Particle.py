import numpy as np # type: ignore

class Particle():

    def __init__(self, m, x, y, vx, vy):
        self.mass = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def distanceTo(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dot(self, other):
        return self.x*other.x + self.y*other.y
    
    def norm(self):
        return np.sqrt(self.dot(self))
    
    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

    def angleTo(self, other):
        if self.x == other.x:
            if self.y > other.y:
                return np.pi*3/2
            elif self.y < other.y:
                return np.pi/2
        
        if self.y == other.y:
            if self.x > other.y:
                return np.pi
            elif self.x < other.y:
                return 0
            
        if self.y > other.y:
            return (np.arctan((other.y - self.y)/(other.x - self.x))) % (2 * np.pi)
        elif self.y < other.y:
            return np.arctan((self.y - other.y)/(other.x - self.x)) + np.pi/2
