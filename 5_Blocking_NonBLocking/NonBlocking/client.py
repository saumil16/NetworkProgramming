import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12344))
client_socket.settimeout(5) # Set timeout for 5 seconds

data_to_send = "Hello!"

try:
    client_socket.sendall(data_to_send.encode())
    print(f"Waiting... - Time: {time.strftime('%H:%M:%S')}")
    time.sleep(5)
    print(f"Timeout ends - Time: {time.strftime('%H:%M:%S')}")
except socket.timeout:
    print(f"Connection timed out - Time: {time.strftime('%H:%M:%S')}")
except Exception as e:
    print(f"Error: {e} - Time: {time.strftime('%H:%M:%S')}")

client_socket.close()