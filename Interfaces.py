from abc import ABC, abstractmethod
from typing import Optional, List
from Domain.Models.models import User, HistoryRecord
from Domain.Models.recipe import Dish

class IUserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]: 
        pass

    @abstractmethod
    def create(self, user: User) -> User: 
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool: 
        pass

    @abstractmethod
    def add_to_history(self, user_id: int, recipe_id: int) -> None: 
        pass

    @abstractmethod
    def get_history(self, user_id: int) -> List[HistoryRecord]: 
        pass

class IDishRepository(ABC):
    @abstractmethod
    def create(self, dish: Dish) -> Dish:
        pass

    @abstractmethod
    def get_all(self) -> List[Dish]:
        pass

    @abstractmethod
    def get_by_id(self, dish_id: int) -> Optional[Dish]:
        pass

    @abstractmethod
    def update(self, dish: Dish) -> Dish:
        pass

    @abstractmethod
    def delete(self, dish_id: int) -> bool:
        pass
