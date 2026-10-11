import hashlib
import secrets

class SecurityUtils:
    @staticmethod
    def generate_salt():
        return secrets.token_hex(16)

    @staticmethod
    def hash_passphrase(passphrase, salt):
        return hashlib.sha256((passphrase + salt).encode()).hexdigest()
