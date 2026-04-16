import time
from functools import wraps
from fastapi import Request, HTTPException
from app.config import settings
from app.utils.logger import logger

failure_count = 0
last_failure_time = 0


# circuit breaker
def circuit_breaker(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        global failure_count, last_failure_time

        # If too many failures → block calls
        if failure_count >= 3:
            if time.time() - last_failure_time < 60:
                logger.error("Circuit breaker active - skipping API call")
                return {}

        try:
            result = await func(*args, **kwargs)
            failure_count = 0  
            return result

        except Exception as error:
            failure_count += 1
            last_failure_time = time.time()
            logger.error(f"API failed: {error}")
            return {}

    return wrapper


# API key validation
def require_api_key(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")

        # fallback: find request in args
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
            logger.warning("Unauthorized access attempt")
            raise HTTPException(
                status_code=401,
                detail="Unauthorized"
            )

        return await func(*args, **kwargs)

    return wrapper