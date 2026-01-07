from os import urandom
from database.connection import execute_query
from utils.crypto import generate_hash


class User:
    def __init__(self, username: str, master_password: str, salt: bytes = None) -> None:
        self.username = username
        self.master_password_hash = generate_hash(master_password)
        self.salt = salt or urandom(32)

    def create_user(self) -> bool:
        try:
            response = execute_query(
                query="SELECT * FROM users WHERE username = ?",
                params=(self.username,)
            )

            if response != []:
                return False

            execute_query(
                query="INSERT INTO users (username, master_password_hash, salt) VALUES (?, ?, ?)",
                params=(self.username, self.master_password_hash, self.salt)
            )
            
            return True

        except Exception as e:
            return False
