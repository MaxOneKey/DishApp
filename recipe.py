from dataclasses import dataclass

@dataclass
class Dish:
    id: int = None
    name: str = ""
    cooking_time: int = 0
    description: str = ""
