from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import User
from interfaces import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_username(self, username: str) -> Optional[User]:
        query = select(User).where(User.username == username)
        return self.session.execute(query).scalars().first()