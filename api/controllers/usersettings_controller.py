from fastapi import APIRouter, HTTPException, Depends
from .auth import validate_token

from models.usersettings import UserSettings
from logic.usersettings_logic import UserSettingsLogic

router = APIRouter()
logic = UserSettingsLogic()

@router.post("/", response_model=UserSettings)
async def create_usersetting(usersetting: UserSettings, claims: str = Depends(validate_token)):
    return logic.create_usersetting(usersetting)

@router.get("/{user_id}", response_model=UserSettings)
async def get_usersetting(user_id: str, claims: str = Depends(validate_token)):
    usersetting = logic.get_usersetting_by_id(user_id)
    if usersetting is None:
        raise HTTPException(status_code=404, detail="UserSetting not found")
    return usersetting

@router.put("/{user_id}", response_model=UserSettings)
async def update_usersetting(user_id: str, usersetting: UserSettings, claims: str = Depends(validate_token)):
    updated_usersetting = logic.update_usersetting(user_id, usersetting)
    if updated_usersetting is None:
        raise HTTPException(status_code=404, detail="UserSetting not found")
    return updated_usersetting

@router.delete("/{user_id}", response_model=UserSettings)
async def delete_usersetting(user_id: str, claims: str = Depends(validate_token)):
    deleted_usersetting = logic.delete_usersetting(user_id)
    if deleted_usersetting is None:
        raise HTTPException(status_code=404, detail="UserSetting not found")
    return deleted_usersetting
