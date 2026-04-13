from interfaces import IUserRepository
from models import User
from typing import Optional

class AuthService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo
        self.current_user: Optional[User] = None

    def login(self, username: str, password: str) -> User:
        user = self.user_repo.get_by_username(username)
        
        if not user or user.password != password:
            raise ValueError("Неправильний логін або пароль")
            
        self.current_user = user
        return self.current_user

    def logout(self) -> None:
        if not self.current_user:
            raise ValueError("Юзер ще не увійшов")
        self.current_user = None

    def switch_account(self, new_username: str, new_password: str) -> User:
        if self.current_user:
            self.logout()
        return self.login(new_username, new_password)