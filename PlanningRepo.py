import sqlite3
from typing import List
from Domain.Models.models import MealPlanItem

class PlanningRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._migrate_and_create()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _migrate_and_create(self):
        with self._get_connection() as conn:
            # 1. Правильна міграція: додаємо колонку статично, потім оновлюємо
            try:
                conn.execute("ALTER TABLE recipes ADD COLUMN calories INTEGER DEFAULT 0")
                # Якщо колонка успішно додалась, заповнюємо всі 0 випадковими калоріями
                conn.execute("UPDATE recipes SET calories = (ABS(RANDOM()) % 600 + 200) WHERE calories = 0")
            except sqlite3.OperationalError:
                pass # Якщо помилка - колонка вже існує, йдемо далі

            conn.execute("""
                CREATE TABLE IF NOT EXISTS meal_plans (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    recipe_id INTEGER NOT NULL,
                    target_date DATE NOT NULL,
                    meal_type TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
                )
            """)

    def add_to_plan(self, user_id: int, recipe_id: int, target_date: str, meal_type: str) -> None:
        with self._get_connection() as conn:
            conn.execute(
                "INSERT INTO meal_plans (user_id, recipe_id, target_date, meal_type) VALUES (?, ?, ?, ?)",
                (user_id, recipe_id, target_date, meal_type)
            )

    def get_plan_by_date(self, user_id: int, target_date: str) -> List[MealPlanItem]:
        plan = []
        with self._get_connection() as conn:
            cursor = conn.execute("""
                SELECT p.id, p.target_date, p.meal_type, r.name, r.cooking_time, r.calories
                FROM meal_plans p
                JOIN recipes r ON p.recipe_id = r.id
                WHERE p.user_id = ? AND p.target_date = ?
                ORDER BY 
                    CASE p.meal_type
                        WHEN 'Сніданок' THEN 1
                        WHEN 'Обід' THEN 2
                        WHEN 'Вечеря' THEN 3
                        ELSE 4
                    END
            """, (user_id, target_date))
            
            for row in cursor.fetchall():
                plan.append(MealPlanItem(
                    id=row[0], date=row[1], meal_type=row[2], 
                    recipe_name=row[3], cooking_time=row[4], calories=row[5]
                ))
        return plan
        
    def delete_from_plan(self, plan_id: int, user_id: int) -> bool:
        with self._get_connection() as conn:
            cursor = conn.execute("DELETE FROM meal_plans WHERE id = ? AND user_id = ?", (plan_id, user_id))
            return cursor.rowcount > 0
        
    def clone_plan(self, user_id: int, source_date: str, target_date: str) -> None:
        with self._get_connection() as conn:
            conn.execute("""
                INSERT INTO meal_plans (user_id, recipe_id, target_date, meal_type)
                SELECT user_id, recipe_id, ?, meal_type
                FROM meal_plans
                WHERE user_id = ? AND target_date = ?
            """, (target_date, user_id, source_date))