from pydantic import BaseModel, Field, EmailStr

class RegistrationSchema(BaseModel):

    username: str = Field(max_length=30)

    email: EmailStr = Field(max_length=100)

    password: str = Field(max_length=255)


class LoginSchema(BaseModel):

    email: EmailStr = Field(max_length=100)

    password: str = Field(max_length=255)