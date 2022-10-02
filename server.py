import socket

from loguru import logger

import config as socket_config


def init_socket() -> socket.socket:
    """Create and configure socket."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    config = socket_config.read()
    sock.bind(config)
    sock.listen()
    logger.debug('[SOCKET] Socket is created')
    return sock


def run(sock: socket.socket):
    """Serve socket."""
    while True:
        conn, addr = sock.accept()
        with conn:
            logger.debug('[CONNECTION] Got connection with {}'.format(addr))
            while True:
                data = conn.recv(1024)
                logger.debug('[DATA] Received: `{}`'.format(data))
                conn.sendall(data)
                stop = input('Stop?\n')
                if stop == 'y':
                    conn.close()
                    break


if __name__ == "__main__":
    sock = init_socket()
    run(sock)
