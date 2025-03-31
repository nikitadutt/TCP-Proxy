# TCP Ping-Pong with Proxy Server  

This project implements a **ping-pong client-server model** using **TCP sockets** with an **intermediate proxy server**. Instead of direct communication between the client and server, all messages must pass through the proxy.  

## Overview  
- The client sends a **4-character string** (not limited to just "ping" or "pong") to the proxy.  
- The proxy forwards the request to the **destination server** (unless the server's IP is blocklisted).  
- The server responds to the message.  
- The proxy forwards the response back to the client.  

## Data Format  
The client sends data to the proxy in **JSON format**:  
```json
{
  "server_ip": "127.0.0.1",
  "server_port": 7000,
  "message": "ping"
}
```
## How to Run
1. In a terminal, use "python server.py" or "python3 server.py" depending on your version of Python.
2. Next, run "python3 proxy.py" in a new terminal.
3. Lastly, run "python3 client.py" in a separate terminal.
4. Once the client starts, it should prompt you to enter a 4-letter input, of which the user should enter an alphabetical string of 4 characters.
5. Refer back to the client, proxy, and server terminals for the output messages.

