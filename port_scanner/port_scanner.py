import sys
import socket
import argparse


def is_port_open(target: str, port: int, timeout: float=0.5)->bool:
    try:
        targetip= socket.gethostbyname(target)
    except Exception as e:
        raise ValueError(f"Could not resolve target '{target}' : {e}")