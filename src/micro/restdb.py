import logging
import httpx

import config

logger = logging.getLogger(__name__)


class RESTDB:

    async def rest_get(url: str, params: dict) -> dict:
        async with httpx.AsyncClient() as client:
            try:
                r = await client.get(
                    f"{config.DATABASE_URL}{url}",
                    params=params,
                    timeout=10.0,
                )
                return r.json()
            except Exception as e:
                # Получить user token
                logger.error(f"{e=}")

    async def fetchall(query: str) -> dict:
        return await RESTDB.rest_get(
            "select",
            {
                "query": query,
            },
        )

    async def get_data(event_type: str, id: int):
        return await RESTDB.rest_get(
            "data",
            {
                "table": event_type,
                "id": id,
            },
        )
