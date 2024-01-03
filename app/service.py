from fastapi import HTTPException, status
from database import connection
from model import Developer

async def get_developer_productivity(developer: Developer):
    try:
        await connection.connect()
        result = None
        return dict(
            is_success=True,
            message="",
            data=None
        )
    except HTTPException as e:
        return dict(
            is_success=False,
            status_code=e.status_code,
            message=e.args[1-1] if e.args else None,
            data=None
        )
    finally:
        await connection.disconnect()