import time
from functools import wraps
from fastapi import Request, HTTPException
from app.config import settings


failure_count = 0
last_failure_time = 0


def circuit_breaker(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        global failure_count, last_failure_time

        if failure_count >= 3:
            if time.time() - last_failure_time < 60:
                print("Circuit breaker active")
                return {}

        try:
            result = await func(*args, **kwargs)
            failure_count = 0
            return result

        except Exception as error:
            failure_count += 1
            last_failure_time = time.time()
            print("API failed:", error)
            return {}

    return wrapper


def require_api_key(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")

        if request is None:
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break

        if not request:
            raise HTTPException(
                status_code=400,
                detail="Request missing"
            )

        api_key = request.headers.get("x-api-key")

        if api_key != settings.API_KEY:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized"
            )

        return await func(*args, **kwargs)

    return wrapper