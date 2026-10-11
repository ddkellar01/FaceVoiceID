from fastapi import FastAPI, HTTPException
from src.models import AuthResponse
from src.db_manager import DBManager
from src.face_engine import FaceEngine
from src.voice_engine import VoiceEngine

app = FastAPI(title="FaceVoiceID API", version="1.0.0")

@app.get("/")
def read_root():
    return {"service": "FaceVoiceID Biometric Authentication API", "status": "active"}

@app.post("/auth/{username}", response_model=AuthResponse)
def authenticate(username: str):
    creds = DBManager.load_credentials(username)
    if not creds:
        raise HTTPException(status_code=404, detail=f"User '{username}' not found.")
    
    face_eng = FaceEngine()
    voice_eng = VoiceEngine()
    
    face_passed = face_eng.verify_face(creds["face"])
    if not face_passed:
        return AuthResponse(status="failed", message="Face verification failed", username=username)
        
    voice_passed = voice_eng.verify_voice(creds["voice"])
    if not voice_passed:
        return AuthResponse(status="failed", message="Voice verification failed", username=username)
        
    return AuthResponse(status="success", message="Multi-factor authentication granted", username=username)
