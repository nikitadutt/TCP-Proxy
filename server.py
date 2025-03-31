import socket
import json

server_ip = '127.0.0.1'
server_port = 54321

server_sock = socket. socket (socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((server_ip, server_port))
server_sock.listen()
while True:
    #receive client data
    conn, addr = server_sock.accept()
    data = conn.recv(1024)
    potential_close_signal = data.decode('utf-8')
    json_data = json.loads(data.decode('utf-8'))
    proxy_ip = json_data.get("proxy_ip")
    proxy_port = json_data.get("proxy_port")
    print(f"Server received data from proxy {proxy_ip}:{proxy_port} = {data.decode('utf-8' )}")
    print(f"Server received message from proxy {proxy_ip}:{proxy_port} = {json_data['message']}\n")

    #send response to client via Proxy
    json_data["Server response"] = "pong"
    print(f"Server added response \"pong\" to the data")
    print(f"Server sent modified data to client via Proxy: {json_data}")
    conn.send(json.dumps(json_data).encode( 'utf-8')
