from typing import Optional
from datetime import datetime


class Password:
    def __init__(
        self,
        id: int,
        user_id: int,
        type_id: Optional[int],
        service: str,
        login: Optional[str],
        iv: bytes,
        password_encrypted: bytes,
        url: Optional[str],
        notes: Optional[str],
        created_at: datetime,
        updated_at: Optional[datetime],
        deleted_at: Optional[datetime],
    ):
        self.id = id
        self.user_id = user_id
        self.type_id = type_id
        self.service = service
        self.login = login
        self.iv = iv
        self.password_encrypted = password_encrypted
        self.url = url
        self.notes = notes
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
