import cv2
import face_recognition
import numpy as np
from src.logger import setup_logger

logger = setup_logger("FaceEngine")

class FaceEngine:
    def __init__(self, tolerance=0.6):
        self.tolerance = tolerance

    def capture_and_encode(self, save_path):
        cap = cv2.VideoCapture(0)
        logger.info("Position your face in front of the camera. Press 's' to capture.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Face Enrollment - Press "s" to capture', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite(save_path, frame)
                break
                
        cap.release()
        cv2.destroyAllWindows()
        
        image = face_recognition.load_image_file(save_path)
        encodings = face_recognition.face_encodings(image)
        
        if len(encodings) > 0:
            logger.info("Face successfully captured and encoded.")
            return encodings[0]
        raise ValueError("No face detected in the captured image.")

    def verify_face(self, known_encoding):
        cap = cv2.VideoCapture(0)
        logger.info("Verifying face... Look at the camera.")
        
        verified = False
        ret, frame = cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_encodings = face_recognition.face_encodings(rgb_frame)
            
            if face_encodings:
                match = face_recognition.compare_faces([known_encoding], face_encodings[0], tolerance=self.tolerance)
                verified = match[0]
                
        cap.release()
        return verified
