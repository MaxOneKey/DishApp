import re
from Domain.Models.models import User
from BusinessLogic.Interfaces import IUserRepository

class AuthService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo
        self.current_user = None

    def register(self, username, password):
        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
            raise ValueError("Помилка: Логін має містити лише латинські літери, цифри або '_', довжина 3-20.")
        

        if not re.match(r"^[a-zA-Z0-9!@#$%^&*()_+]{6,30}$", password):
            raise ValueError("Помилка: Недопустимий формат пароля (мінімум 6 символів).")

        if self.user_repo.get_by_username(username):
            raise ValueError("Помилка: Користувач з таким іменем вже існує.")
            
        new_user = User(username=username, password=password)
        return self.user_repo.create(new_user)

    def login(self, username, password):
        user = self.user_repo.get_by_username(username)
        if not user or user.password != password:
            raise ValueError("Помилка: Неправильний логін або пароль.")
        self.current_user = user
        return user

    def logout(self):
        if not self.current_user:
            raise ValueError("Помилка: Ви ще не увійшли.")
        self.current_user = None

    def switch_account(self, new_username, new_password):
        if self.current_user:
            self.logout()
        return self.login(new_username, new_password)

    def delete_account(self):
        if not self.current_user:
            raise ValueError("Помилка: Немає активного акаунта для видалення.")
        self.user_repo.delete(self.current_user.id)
        self.logout()
    
    def record_cooking(self, recipe_id: int):
        if not self.current_user:
            raise ValueError("Потрібно увійти в акаунт.")
        self.user_repo.add_to_history(self.current_user.id, recipe_id)

    def get_my_history(self):
        if not self.current_user:
            raise ValueError("Потрібно увійти в акаунт.")
        return self.user_repo.get_history(self.current_user.id)
