from types import FunctionType


class Events:

    @classmethod
    async def do(cls, js):
        for name, func in cls.__dict__.items():
            if type(func) is FunctionType and (
                ("_".join(js["event"].split("."))) + "_"
            ).startswith(f"{name}_"):
                event_split = js["event"].split(".")
                await func(
                    [
                        event_split[i] if i < len(event_split) else ""
                        for i in range(0, 10)
                    ],
                    js,
                )
