from pydantic import BaseModel, Field

class UserRegistrationRequest(BaseModel):
    username: str = Field(..., description="Unique user identifier")

class AuthResponse(BaseModel):
    status: str
    message: str
    username: str
