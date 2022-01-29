from pydantic import BaseModel, validator
from src.enums.user_enums import Gender, Status, UserError

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status

    @validator('email')
    def check_email_is_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserError.WRONG_EMAIL.value)