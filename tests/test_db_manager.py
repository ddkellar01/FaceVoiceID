import os
import pytest
from src.db_manager import DBManager
from src.config import CREDS_DIR

def test_db_save_and_load(tmp_path):
    # Temporarily override creds directory for testing
    import src.db_manager
    original_creds_dir = src.db_manager.CREDS_DIR
    src.db_manager.CREDS_DIR = str(tmp_path)
    
    try:
        username = "testuser"
        mock_creds = {"face": [0.1] * 128, "voice": [0.5] * 40}
        
        DBManager.save_credentials(username, mock_creds)
        loaded = DBManager.load_credentials(username)
        
        assert loaded is not None
        assert "face" in loaded
        assert "voice" in loaded
        assert loaded["face"] == mock_creds["face"]
    finally:
        src.db_manager.CREDS_DIR = original_creds_dir
