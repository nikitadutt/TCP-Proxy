import socket 
import json

server_ip = "127.0.0.1"
server_port = 54321
proxy_ip = '127.0.0.1'
proxy_port = 65432

while True:
    client_sock= socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((proxy_ip, proxy_port))
    while True:
        message = input("Enter a four-letter word: ")  # Get input from user
        
        # Ensure it's a four-letter word
        if len(message) == 4 and message.isalpha():
            break
        else:
            print("Error: Message must be exactly four letters. Try again.")

    data = {
    "server_ip": server_ip,
    "server_port": server_port,
    "message": message
    }

    #send data from client to proxy
    client_sock.send(json.dumps (data).encode( 'utf-8'))
    print(f"Client sent json data to Proxy {proxy_ip}:{proxy_port} = {data} ")
    print(f"Client sent message \"{message}\" to Proxy {proxy_ip}:{proxy_port}\n")

    #receive data from server to proxy
    data = client_sock.recv(1024)
    json_list = json.loads(data.decode ('utf-8' ))
    print(f"Client received response from Proxy {proxy_ip}:{proxy_port} sent by Server {server_ip}:{server_port} = {json_list['Server response']}")
    print(f"Client received json data from Proxy {proxy_ip}:{proxy_port} sent by Server {server_ip}:{server_port} = {json_list}") 
