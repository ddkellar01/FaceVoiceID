import pytest
from unittest.mock import MagicMock, patch
from src.face_engine import FaceEngine

def test_face_engine_initialization():
    engine = FaceEngine(tolerance=0.5)
    assert engine.tolerance == 0.5

@patch("cv2.VideoCapture")
def test_verify_face_no_frame(mock_video_capture):
    mock_cap = MagicMock()
    mock_cap.read.return_value = (False, None)
    mock_video_capture.return_value = mock_cap
    
    engine = FaceEngine()
    result = engine.verify_face(known_encoding=[0.1] * 128)
    assert result is False
