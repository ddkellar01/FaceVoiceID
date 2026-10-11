from src.security import SecurityUtils

def test_salt_generation():
    salt1 = SecurityUtils.generate_salt()
    salt2 = SecurityUtils.generate_salt()
    assert salt1 != salt2
    assert len(salt1) == 32

def test_passphrase_hashing():
    salt = "test_salt"
    hash1 = SecurityUtils.hash_passphrase("securepass", salt)
    hash2 = SecurityUtils.hash_passphrase("securepass", salt)
    hash3 = SecurityUtils.hash_passphrase("differentpass", salt)
    
    assert hash1 == hash2
    assert hash1 != hash3
