from typing import Optional
from datetime import datetime


class PasswordHistory:
    def __init__(
        self,
        id: int,
        password_id: Optional[int],
        user_id: int,
        type_id: Optional[int],
        service: str,
        login: Optional[str],
        iv: bytes,
        encrypted_password: bytes,
        url: Optional[str],
        notes: Optional[str],
        changed_at: datetime,
    ):
        self.id = id
        self.password_id = password_id
        self.user_id = user_id
        self.type_id = type_id
        self.service = service
        self.login = login
        self.iv = iv
        self.encrypted_password = encrypted_password
        self.url = url
        self.notes = notes
        self.changed_at = changed_at
