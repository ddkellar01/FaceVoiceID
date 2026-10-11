import numpy as np

class AudioPreprocessor:
    @staticmethod
    def normalize_audio(audio: np.ndarray) -> np.ndarray:
        """Normalizes audio signal amplitude."""
        max_val = np.max(np.abs(audio))
        if max_val > 0:
            return audio / max_val
        return audio
