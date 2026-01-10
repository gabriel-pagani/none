import re


def validate_master_password(master_password: str) -> bool:
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{12,}$"
    return bool(re.match(pattern, master_password))
