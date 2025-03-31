import socket 
import json

blocklist = ["192.168.1.1", "10.0.0.1"]
proxy_ip = '127.0.0.1'
proxy_port = 65432

proxy_sock = socket. socket (socket.AF_INET, socket.SOCK_STREAM)
proxy_sock.bind( (proxy_ip, proxy_port))
proxy_sock.listen( )
while True:
    #receive data from client
    client_conn, client_addr = proxy_sock.accept()
    data = client_conn.recv (1024)
    json_list = json.loads(data.decode ('utf-8' ))
    server_ip = json_list["server_ip"]
    server_port = json_list["server_port"]
    print (f"Proxy received data from client {client_addr} = {json_list}")
    print (f"Proxy received message from client {client_addr} = {json_list["message"]}")
    print(f"Proxy received server IP {server_ip} and server port {server_port} from client {client_addr}\n")
    if server_ip in blocklist:
        client_conn.send(b"Error")
        print (f"Blocked IP: {server_ip}")
    else:
        #add proxy's IP and Port to the data so server can extract it
        json_list["proxy_ip"] = proxy_ip
        json_list["proxy_port"] = proxy_port
        print(f"Proxy added proxy IP {proxy_ip} and port number {proxy_port} to the data")

        #connect Proxy and Server so Proxy can forward Client's data to Server
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.connect((server_ip, json_list ["server_port"])) 
        server_sock.send(json.dumps(json_list).encode( 'utf-8'))
        print(f"Proxy sent modified data to server {server_ip}:{server_port} from client {client_addr} = {json_list}\n")
        
        #receive response from Server
        response = server_sock.recv (1024)
        json_data_from_server = json.loads(response.decode ('utf-8' ))
        server_ip = json_data_from_server["server_ip"]
        server_port = json_data_from_server["server_port"]
        print (f"Proxy received data from server {server_ip}:{server_port} = {response.decode ('utf-8')}")
        print(f"Proxy received message from server {server_ip}:{server_port} = {json_data_from_server["Server response"]}\n")

        #send data from server to client
        client_conn.send(response)
        print(f"Proxy sent data from server {server_ip}:{server_port} back to client {client_addr}= {json_data_from_server}")
        print(f"Proxy sent message from server {server_ip}:{server_port} back to client {client_addr}= {json_data_from_server["Server response"]}")
