from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

p1 = Point3D(1, 2, 3)
print(p1)

try:
    p1.x = 10
except AttributeError as e:
    print(f"Mistake: {e}")