from fastapi import FastAPI
import os
import redis
import socket

app = FastAPI()
redis_host = os.environ.get("REDIS_HOST") or "host.docker.internal"
cache = redis.client.Redis(host=redis_host)


@app.get("/")
async def root():
    return {
        "hello": "world",
        "hits": cache.incr("hits"),
        "app_hostname": socket.gethostname(),
        "redis_hostname": redis_host,
    }
