from authx import AuthX, AuthXConfig

JWT_SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

authx = AuthX(JWT_SECRET_KEY)
