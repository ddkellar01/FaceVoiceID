# Architecture Overview

FaceVoiceID utilizes a two-tier biometric verification pipeline combining computer vision and acoustic feature extraction.

```mermaid
graph TD
    A[Live Input Feed] --> B[Face Engine: OpenCV & face_recognition]
    A --> C[Voice Engine: SoundDevice & Librosa]
    B --> D{Face Match? < 0.6}
    C --> E{Voice Match? Euclidean < 15.0}
    D -- Yes --> F[Multi-Factor Gate]
    E -- Yes --> F
    F --> G[Access Granted / JWT Token Issued]
    D -- No --> H[Access Denied]
    E -- No --> H
