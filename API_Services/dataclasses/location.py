from dataclasses import dataclass

@dataclass
class Location:
    longitude: float
    latitude: float
    
    def __post_init__(self):
        self.longitude_min = self.longitude - 0.25
        self.longitude_max = self.longitude + 0.25
        self.latitude_min = self.latitude - 0.25
        self.latitude_max = self.latitude + 0.25