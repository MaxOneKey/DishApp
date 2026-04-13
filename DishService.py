from interfaces import IDishRepository
from models import Dish
from typing import List
import random

class DishService:
    def __init__(self, dish_repo: IDishRepository):
        self.dish_repo = dish_repo

    def create_dish(self, name: str, price: float, description: str) -> Dish:
        if price <= 0:
            raise ValueError("Ціна < 0")
            
        new_dish = Dish(id=0, name=name, price=price, description=description)
        return self.dish_repo.create(new_dish)

    def get_all_dishes(self) -> List[Dish]:
        return self.dish_repo.get_all()

    def get_dish(self, dish_id: int) -> Dish:
        dish = self.dish_repo.get_by_id(dish_id)
        if not dish:
            raise ValueError(f"Страву не знайдено")
        return dish

    def update_dish(self, dish_id: int, name: str, price: float, description: str) -> Dish:
        dish = self.get_dish(dish_id)
        
        if price <= 0:
            raise ValueError("Ціна < 0")
            
        dish.name = name
        dish.price = price
        dish.description = description
        
        return self.dish_repo.update(dish)

    def delete_dish(self, dish_id: int) -> bool:
        self.get_dish(dish_id)
        return self.dish_repo.delete(dish_id)
    
    def roll_random_dish(self) -> Dish:
        all_dishes = self.dish_repo.get_all()
        
        if not all_dishes:
            raise ValueError("Меню пусте")
        return random.choice(all_dishes)