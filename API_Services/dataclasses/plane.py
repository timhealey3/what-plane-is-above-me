from dataclasses import dataclass

@dataclass
class Plane:
    tailNumber: str
    make: str
    model: str
    owner: str