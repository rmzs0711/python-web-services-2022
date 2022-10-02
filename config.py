import os
from typing import NamedTuple
from dotenv import load_dotenv


class SocketConf(NamedTuple):
    """Socket configuration."""
    host: str
    port: int


def read() -> SocketConf:
    """Populate `SocketConf`."""
    load_dotenv()
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    try:
        port = int(port)
    except ValueError:
        raise Exception('Port must be integer')
    return SocketConf(host, port)
