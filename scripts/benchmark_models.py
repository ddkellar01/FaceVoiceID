import time
import numpy as np
from src.voice_engine import VoiceEngine

def benchmark_voice_extraction():
    engine = VoiceEngine()
    dummy_audio = np.random.randn(22050 * 3)
    
    start_time = time.time()
    for _ in range(100):
        engine.extract_features(dummy_audio)
    duration = time.time() - start_time
    
    print(f"Benchmark: 100 MFCC extractions took {duration:.4f} seconds.")

if __name__ == "__main__":
    benchmark_voice_extraction()
