from fastapi import Depends, HTTPException
from app.auth.auth import get_current_active_user
from app.models import User


def get_current_admin_user(current_user: User = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user
