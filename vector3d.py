
from dataclasses import dataclass
from math import sqrt


@dataclass
class Vector3D:
    x: float
    y: float
    z: float

    def len(self):
        return sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    
    def unit(self):
        n = self.len()
        return Vector3D(self.x / n, self.y / n, self.z / n)
    
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    
    
