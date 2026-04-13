from abc import ABC, abstractmethod
from typing import List, Optional
from models import User, Dish

class IUserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
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