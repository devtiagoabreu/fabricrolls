# admin.py
class UserManager:
    def add_user(self, username: str, password: str, is_admin: bool):
        encrypted = encrypt_password(password)
        # Salva no banco de dados...