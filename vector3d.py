
from dataclasses import dataclass
from math import sqrt


@dataclass
class Vector3D:
    x: float
    y: float
    z: float

    def len(self):
        return sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    
