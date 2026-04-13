from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    password: str 

@dataclass
class Dish:
    id: int
    name: str
    price: float
    description: str