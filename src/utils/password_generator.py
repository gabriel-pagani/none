import secrets


def generate_password() -> str:
    characters = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&-_=~^,.<>;:()[]{}"
    password = ''.join(secrets.choice(characters) for _ in range(50))
    return password
