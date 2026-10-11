import os
import pickle
from src.config import CREDS_DIR, FACES_DIR, VOICES_DIR
from src.logger import setup_logger

logger = setup_logger("DBManager")

class DBManager:
    @staticmethod
    def initialize_storage():
        os.makedirs(CREDS_DIR, exist_ok=True)
        os.makedirs(FACES_DIR, exist_ok=True)
        os.makedirs(VOICES_DIR, exist_ok=True)

    @staticmethod
    def save_credentials(username, credentials):
        DBManager.initialize_storage()
        path = os.path.join(CREDS_DIR, f"{username}.pkl")
        with open(path, "wb") as f:
            pickle.dump(credentials, f)
        logger.info(f"Credentials saved for user: {username}")

    @staticmethod
    def load_credentials(username):
        path = os.path.join(CREDS_DIR, f"{username}.pkl")
        if not os.path.exists(path):
            return None
        with open(path, "rb") as f:
            return pickle.load(f)
