from Repositories.PlanningRepo import PlanningRepository
from typing import Dict, Any

class PlanningService:
    def __init__(self, plan_repo: PlanningRepository, auth_service):
        self.plan_repo = plan_repo
        self.auth_service = auth_service
        self.MAX_MEALS_PER_DAY = 6  # Захист від абсурдних значень

    def add_meal(self, recipe_id: int, target_date: str, meal_type: str):
        if not self.auth_service.current_user:
            raise ValueError("Потрібно увійти в акаунт.")
        
        valid_types = ["Сніданок", "Обід", "Вечеря", "Перекус"]
        if meal_type not in valid_types:
            raise ValueError(f"Невірний тип прийому їжі. Доступні: {', '.join(valid_types)}")
            
        # Перевірка на ліміт
        current_plan = self.plan_repo.get_plan_by_date(self.auth_service.current_user.id, target_date)
        if len(current_plan) >= self.MAX_MEALS_PER_DAY:
            raise ValueError(f"Досягнуто ліміт! Максимум {self.MAX_MEALS_PER_DAY} страв на день.")

        self.plan_repo.add_to_plan(self.auth_service.current_user.id, recipe_id, target_date, meal_type)

    def remove_meal(self, plan_id: int):
        if not self.auth_service.current_user:
            raise ValueError("Потрібно увійти в акаунт.")
        
        success = self.plan_repo.delete_from_plan(plan_id, self.auth_service.current_user.id)
        if not success:
            raise ValueError("Страву не знайдено у вашому плані (або невірний ID).")

    def clone_day(self, source_date: str, target_date: str):
        if not self.auth_service.current_user:
            raise ValueError("Потрібно увійти в акаунт.")
            
        source_items = self.plan_repo.get_plan_by_date(self.auth_service.current_user.id, source_date)
        if not source_items:
            raise ValueError(f"План на {source_date} порожній, нічого клонувати.")
        
        target_items = self.plan_repo.get_plan_by_date(self.auth_service.current_user.id, target_date)
        
        # Перевіряємо, чи після злиття планів не буде перевищено ліміт
        if len(target_items) + len(source_items) > self.MAX_MEALS_PER_DAY:
            raise ValueError(f"Клонування неможливе: разом вийде більше {self.MAX_MEALS_PER_DAY} страв на день.")

        self.plan_repo.clone_plan(self.auth_service.current_user.id, source_date, target_date)

    def get_daily_summary(self, target_date: str) -> Dict[str, Any]:
        if not self.auth_service.current_user:
            raise ValueError("Потрібно увійти в акаунт.")
            
        items = self.plan_repo.get_plan_by_date(self.auth_service.current_user.id, target_date)
        
        total_calories = sum(item.calories for item in items)
        total_time = sum(item.cooking_time for item in items)
        
        return {
            "date": target_date,
            "items": items,
            "total_calories": total_calories,
            "total_cooking_time": total_time
        }