from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def list_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]