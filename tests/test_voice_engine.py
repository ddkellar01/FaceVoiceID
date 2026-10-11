import pytest
import numpy as np
from src.voice_engine import VoiceEngine

def test_voice_engine_initialization():
    engine = VoiceEngine(sample_rate=16000, duration=2)
    assert engine.sample_rate == 16000
    assert engine.duration == 2

def test_extract_features_shape():
    engine = VoiceEngine(sample_rate=22050, duration=1)
    dummy_audio = np.random.randn(22050)
    features = engine.extract_features(dummy_audio)
    assert features.shape == (40,)
