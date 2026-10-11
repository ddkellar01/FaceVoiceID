# API Reference

## Base URL
`http://localhost:8000`

---

## Endpoints

### 1. Health Check
* **URL:** `/`
* **Method:** `GET`
* **Description:** Verifies that the FastAPI biometric service is online and operational.
* **Response Example:**
  ```json
  {
    "service": "FaceVoiceID Biometric Authentication API",
    "status": "active"
  }
