# HOW TO MIGRATE DB: 

# cd FastAPI/pkg/db/migrations

# alembic revision --autogenerate -m "Commit name"

# alembic upgrade head

# connect db, add it to .env file -> DATABASE_URL = "postgresql://postgres: PASSWORD @localhost:5432/ DB NAME" example: postgresql://postgres:12345@localhost:5432/FastAPI_project

# in alembic.ini: sqlalchemy.url = postgresql://postgres:12345@localhost:5432/FastAPI_project

# in alembic env.py: 

# from FastAPI.pkg.db.database import Base
# from FastAPI.pkg.db.models import ExampleModel

# target_metadata = Base.metadata


# .env like = DATABASE_URL = "postgresql://postgres:password@localhost:host/template"
