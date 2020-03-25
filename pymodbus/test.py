from pyModbusTCP.client import ModbusClient
from pyModbusTCP.server import ModbusServer
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 502))
s.listen(5)