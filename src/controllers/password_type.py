from typing import Optional
from database.connection import execute_query


class PasswordType:
    def __init__(
        self, 
        id: int, 
        name: str
    ):
        self.id = id
        self.name = name

    @classmethod
    def get(cls, id: int) -> Optional['PasswordType']:
        try:
            response = execute_query(
                "SELECT * FROM password_types WHERE id = ?",
                (id,)
            )
            
            if response != []:
                return cls(
                    id=response[0][0], 
                    name=response[0][1],
                )
            return None

        except Exception as e:
            print(f"exception-on-get: {e}")
            return None
