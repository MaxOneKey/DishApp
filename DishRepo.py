from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from Models import Dish
from interfaces import IDishRepository

class DishRepository(IDishRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, dish: Dish) -> Dish:
        self.session.add(dish)
        self.session.commit()
        self.session.refresh(dish)
        return dish

    def get_all(self) -> List[Dish]:
        query = select(Dish)
        return list(self.session.execute(query).scalars().all())

    def get_by_id(self, dish_id: int) -> Optional[Dish]:
        return self.session.get(Dish, dish_id)

    def update(self, dish: Dish) -> Dish:
        self.session.merge(dish)
        self.session.commit()
        return dish

    def delete(self, dish_id: int) -> bool:
        dish = self.get_by_id(dish_id)
        if dish:
            self.session.delete(dish)
            self.session.commit()
            return True
        return False

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from models import Base
    from DishService import DishService

    engine = create_engine("sqlite:///kitchen.db")
    Base.metadata.create_all(engine)
    
    with Session(engine) as session:
        repo = DishRepository(session)
        service = DishService(repo)

        while True:
            print("\n1. Додати | 2. Вивести | 3. Оновити | 4. Видалити | 5. Вийти")
            choice = input("Оберіть дію: ")

            if choice == "1":
                name = input("Назва: ")
                price = float(input("Ціна: "))
                desc = input("Опис: ")
                service.create_dish(name, price, desc)
            
            elif choice == "2":
                for dish in service.get_all_dishes():
                    print(f"[{dish.id}] {dish.name} | {dish.price} грн | {dish.description}")
            
            elif choice == "3":
                d_id = int(input("ID страви: "))
                name = input("Нова назва: ")
                price = float(input("Нова ціна: "))
                desc = input("Новий опис: ")
                service.update_dish(d_id, name, price, desc)
            
            elif choice == "4":
                d_id = int(input("ID страви: "))
                service.delete_dish(d_id)
            
            elif choice == "5":
                break