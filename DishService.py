from Repositories.DishRepo import DishRepository

class DishService:
    def __init__(self, dish_repo: DishRepository):
        self.dish_repo = dish_repo

    def get_trends(self):
        return self.dish_repo.get_trending(limit=3)

    def search(self, keyword: str, max_time_str: str):
        max_time = None
        if max_time_str.isdigit():
            max_time = int(max_time_str)
            if max_time <= 0:
                raise ValueError("Час приготування має бути більшим за 0.")
        
        return self.dish_repo.search_recipes(keyword=keyword, max_time=max_time)
    
    def get_recipe(self, recipe_id: int):
        recipe = self.dish_repo.get_by_id(recipe_id)
        if not recipe:
            raise ValueError("Рецепт не знайдено.")
        return recipe

    def generate_cooking_steps(self, description: str) -> list:
        """Розбиваємо текст на кроки за крапками (найпростіший парсинг)"""
        if not description or description.lower() == 'none':
            return ["Готуйте на свій смак! (Детальний опис відсутній)"]
        
        steps = [step.strip() + "." for step in description.split('.') if step.strip()]
        return steps if steps else [description]
