from fastapi import FastAPI
from pydantic import BaseModel

# API versiyalari uchun katalog
api_v1 = FastAPI(title="API v1", version="1.0")
api_v2 = FastAPI(title="API v2", version="2.0")

# Model uchun katalog
class User(BaseModel):
    id: int
    name: str
    email: str

# API v1 uchun endpointlar
@api_v1.get("/users/")
def get_users():
    return [{"id": 1, "name": "John Doe", "email": "john@example.com"}]

@api_v1.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}

# API v2 uchun endpointlar
@api_v2.get("/users/")
def get_users_v2():
    return [{"id": 1, "name": "John Doe", "email": "john@example.com"}]

@api_v2.get("/users/{user_id}")
def get_user_v2(user_id: int):
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}
```

Bu kodda FastAPI kutubxonasidan foydalanib, ikkita API versiyasi yaratilgan: v1 va v2. Har bir versiyada bir nechta endpointlar mavjud.
