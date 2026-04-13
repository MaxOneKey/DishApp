import sqlite3
from typing import List, Optional
from Domain.Models.models import User, HistoryRecord
from BusinessLogic.Interfaces import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS user_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    recipe_id INTEGER NOT NULL,
                    cooked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (recipe_id) REFERENCES recipes (id)
                )
            """)
            
    def add_to_history(self, user_id: int, recipe_id: int) -> None:
        with self._get_connection() as conn:
            conn.execute("INSERT INTO user_history (user_id, recipe_id) VALUES (?, ?)", (user_id, recipe_id))

    def get_history(self, user_id: int) -> List[HistoryRecord]:
        records = []
        with self._get_connection() as conn:
            cursor = conn.execute("""
                SELECT h.id, r.name, h.cooked_at 
                FROM user_history h
                JOIN recipes r ON h.recipe_id = r.id
                WHERE h.user_id = ?
                ORDER BY h.cooked_at DESC
            """, (user_id,))
            for row in cursor.fetchall():
                records.append(HistoryRecord(id=row[0], recipe_name=row[1], cooked_at=row[2]))
        return records

    def get_by_username(self, username: str) -> Optional[User]:
        with self._get_connection() as conn:
            cursor = conn.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
            row = cursor.fetchone()
            if row:
                return User(id=row[0], username=row[1], password=row[2])
        return None

    def create(self, user: User) -> User:
        with self._get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", 
                (user.username, user.password)
            )
            user.id = cursor.lastrowid
            return user

    def delete(self, user_id: int) -> bool:
        with self._get_connection() as conn:
            cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            return cursor.rowcount > 0
