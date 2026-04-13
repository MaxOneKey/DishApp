import sqlite3
from typing import List, Optional
from Domain.Models.recipe import Dish

class DishRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def get_trending(self, limit: int = 3) -> List[Dish]:
        """Суперпримітивні тренди: беремо випадкові рецепти"""
        recipes = []
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT id, name, cooking_time, description FROM recipes ORDER BY RANDOM() LIMIT ?", 
                (limit,)
            )
            for row in cursor.fetchall():
                recipes.append(Dish(id=row[0], name=row[1], cooking_time=row[2], description=row[3]))
        return recipes

    def search_recipes(self, keyword: str = "", max_time: Optional[int] = None) -> List[Dish]:
        """Пошук за ключовим словом та/або часом"""
        recipes = []
        query = "SELECT id, name, cooking_time, description FROM recipes WHERE 1=1"
        params = []

        if keyword:
            query += " AND (name LIKE ? OR description LIKE ?)"
            params.extend([f"%{keyword}%", f"%{keyword}%"])
        
        if max_time:
            query += " AND cooking_time <= ?"
            params.append(max_time)

        query += " LIMIT 10"

        with self._get_connection() as conn:
            cursor = conn.execute(query, params)
            for row in cursor.fetchall():
                recipes.append(Dish(id=row[0], name=row[1], cooking_time=row[2], description=row[3]))
        return recipes
    
    def get_by_id(self, recipe_id: int) -> Optional[Dish]:
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT id, name, cooking_time, description FROM recipes WHERE id = ?", 
                (recipe_id,)
            )
            row = cursor.fetchone()
            if row:
                return Dish(id=row[0], name=row[1], cooking_time=row[2], description=row[3])
        return None
