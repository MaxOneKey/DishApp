from dataclasses import dataclass

@dataclass
class User:
    id: int = None
    username: str = ""
    password: str = ""

@dataclass
class HistoryRecord:
    id: int
    recipe_name: str
    cooked_at: str

@dataclass
class MealPlanItem:
    id: int
    date: str
    meal_type: str
    recipe_name: str
    cooking_time: int
    calories: int
