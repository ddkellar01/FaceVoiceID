import sounddevice as sd
import numpy as np
import librosa
import scipy.spatial
import soundfile as sf
from src.logger import setup_logger

logger = setup_logger("VoiceEngine")

class VoiceEngine:
    def __init__(self, sample_rate=22050, duration=3):
        self.sample_rate = sample_rate
        self.duration = duration

    def record_audio(self, save_path=None):
        logger.info(f"Recording for {self.duration} seconds... Speak your passphrase.")
        audio = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='float32')
        sd.wait()
        audio = np.squeeze(audio)
        
        if save_path:
            sf.write(save_path, audio, self.sample_rate)
            
        return audio

    def extract_features(self, audio):
        mfccs = librosa.feature.mfcc(y=audio, sr=self.sample_rate, n_mfcc=40)
        return np.mean(mfccs.T, axis=0)

    def verify_voice(self, known_features, threshold=15.0):
        logger.info("Please repeat your passphrase for voice verification...")
        live_audio = self.record_audio()
        live_features = self.extract_features(live_audio)
        
        distance = scipy.spatial.distance.euclidean(known_features, live_features)
        logger.info(f"Voice Distance Score: {distance:.2f}")
        
        return distance < threshold
