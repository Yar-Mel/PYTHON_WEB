from ipaddress import ip_address
from typing import Callable
from fastapi.responses import JSONResponse
from fastapi_limiter import FastAPILimiter
from fastapi import Request, HTTPException, status
import redis.asyncio as redis
import re
from src.config.config import settings


allowed_ips = [ip_address("192.168.1.1"), ip_address("127.0.0.1")]
banned_ips = []
user_agent_ban_list = []


async def startup_event():
    r = await redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        db=0,
        encoding="utf-8",
        decode_responses=True,
    )
    await FastAPILimiter.init(r)


async def limit_access_by_ip_middleware(request: Request, call_next: Callable):
    address = ip_address(request.client.host)
    if address not in allowed_ips:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": "Not allowed IP address"},
        )
    resp = await call_next(request)
    return resp


async def ban_ips_middleware(request: Request, call_next: Callable):
    address = ip_address(request.client.host)
    if address in banned_ips:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are banned"
        )
    resp = await call_next(request)
    return resp


async def user_agent_ban_middleware(request: Request, call_next: Callable):
    user_agent = request.headers.get("user-agent")
    for ban_pattern in user_agent_ban_list:
        if re.search(ban_pattern, user_agent):
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={"detail": "You are banned"},
            )
    resp = await call_next(request)
    return resp
