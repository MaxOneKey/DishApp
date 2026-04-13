from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Recipe

class RecipeDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    # Метод 1: Створити рецепт (Create)
    async def create_recipe(self, name: str, description: str, cooking_time: int):
        new_recipe = Recipe(name=name, description=description, cooking_time=cooking_time)
        self.session.add(new_recipe)
        await self.session.commit()
        return new_recipe

    # Метод 2: Отримати всі рецепти (Read)
    async def get_all_recipes(self):
        query = select(Recipe).order_by(Recipe.name)
        result = await self.session.execute(query)
        return result.scalars().all()

    # Метод 3: Отримати один за ID
    async def get_recipe_by_id(self, recipe_id: int):
        return await self.session.get(Recipe, recipe_id)