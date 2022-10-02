import socket
from loguru import logger

import config as socket_config


def send_messages():
    config = socket_config.read()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        number = 0
        s.connect(config)
        while True:
            try:
                s.sendall(bytes(f'Hello, world {number}', 'utf-8'))
            except:
                logger.error("Unable to send: connection is closed")
                break
            try:
                data = s.recv(1024)
            except:
                logger.error('Unable to recv: connection is closed')
                break
            logger.debug('[RECV] {}'.format(data))
            number += 1


if __name__ == "__main__":
    send_messages()
