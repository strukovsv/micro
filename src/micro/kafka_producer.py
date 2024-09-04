import logging
import json

from aiokafka import AIOKafkaProducer

import config

logger = logging.getLogger(__name__)

producer = None


class KafkaProducer(AIOKafkaProducer):

    def __init__(self):
        if config.PRODUCER_KAFKA["bootstrap_servers"]:
            super().__init__(
                **config.PRODUCER_KAFKA,
                enable_idempotence=config.ENABLE_IDEMPOTENCE,
            )
            logger.info(f"connect producer kafka: {config.PRODUCER_KAFKA}")

    async def send_kafka(self, id, data):
        """Отправить сообщение в kafka"""
        await self.send_and_wait(
            topic=config.DST_TOPIC,
            key=id.to_bytes(8, "big"),
            value=json.dumps(data, ensure_ascii=False).encode(),
        )


async def send_event(message: dict, event: str = None):
    global producer
    js = message.copy()
    _event = event if event else js.get("answer", None)
    if _event:
        if js.get("event", None):
            js["events"] = js.get("events", []) + [js["event"]]
        js["event"] = _event
        logger.info(f'send message "{js}" to "{_event}"')
        await producer.send_kafka(id=0, data=js)
