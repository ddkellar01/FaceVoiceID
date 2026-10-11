import sys
from src.face_engine import FaceEngine
from src.voice_engine import VoiceEngine
from src.db_manager import DBManager
from src.config import FACES_DIR

def register_user(username):
    DBManager.initialize_storage()
    face_path = f"{FACES_DIR}/{username}.jpg"
    
    face_eng = FaceEngine()
    voice_eng = VoiceEngine()
    
    print("\n--- Phase 1: Face Registration ---")
    face_encoding = face_eng.capture_and_encode(face_path)
    
    print("\n--- Phase 2: Voice Registration ---")
    audio = voice_eng.record_audio()
    voice_features = voice_eng.extract_features(audio)
    
    credentials = {
        "face": face_encoding,
        "voice": voice_features
    }
    DBManager.save_credentials(username, credentials)
    print(f"\nUser '{username}' successfully registered!")

def authenticate_user(username):
    creds = DBManager.load_credentials(username)
    if not creds:
        print(f"User '{username}' not found.")
        return

    face_eng = FaceEngine()
    voice_eng = VoiceEngine()
    
    print("\n--- Step 1: Face Verification ---")
    if not face_eng.verify_face(creds["face"]):
        print("❌ Face Authentication Failed!")
        return
    print("✅ Face Verified Successfully!")
    
    print("\n--- Step 2: Voice Verification ---")
    if not voice_eng.verify_voice(creds["voice"]):
        print("❌ Voice Authentication Failed!")
        return
    print("✅ Voice Verified Successfully!")
    print(f"\n🎉 Multi-Factor Access Granted for '{username}'!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python main.py register <username>")
        print("  python main.py auth <username>")
        sys.exit(1)
        
    action = sys.argv[1]
    user = sys.argv[2]
    
    if action == "register":
        register_user(user)
    elif action == "auth":
        authenticate_user(user)
    else:
        print("Unknown action. Use 'register' or 'auth'.")
