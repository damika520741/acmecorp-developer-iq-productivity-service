from fastapi import status
from database import connection
from model import Developer

async def get_developer_productivity(developer: Developer):
    try:
        await connection.connect()
        result = None
        return dict(
            is_success=True,
            status_code= status.HTTP_200_OK,
            message="",
            data=None
        )
    except Exception as e:
        return dict(
            is_success=False,
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data=None
        )
    finally:
        await connection.disconnect()