import asyncio
from fastapi import FastAPI
from db import init_db
from tortoise import Tortoise


def create_app() -> None:
    app = FastAPI(
        title="User",
        version='0.0.1',
        description="FastAPI CRUD Asyncpg",
        debug=True,
    )
    app.include_router(router)
    return app


async def main():
    app = create_app()
    await init_db()
    print("DB Connected ✅")
    await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())
