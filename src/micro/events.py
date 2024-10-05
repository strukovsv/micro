import logging

from types import FunctionType

logger = logging.getLogger(__name__)


class Events:

    @classmethod
    async def do(cls, js):
        for name, func in cls.__dict__.items():
            if type(func) is FunctionType and (
                ("_".join(js["event"].split("."))) + "_"
            ).startswith(f"{name}_"):
                event_split = js["event"].split(".")
                logger.info(f'event: {js["event"]} => {name}')
                await func(
                    [
                        event_split[i] if i < len(event_split) else ""
                        for i in range(0, 10)
                    ],
                    js,
                )
