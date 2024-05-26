#!/usr/bin/python3
"""socket server"""
import socket
import json


def start_server(host='localhost', port=12345):
    """
    Start a server that listens for incoming connections and
    processes received data.

    Parameters:
    host (str): The hostname or IP address to listen on.
    port (int): The port number to listen on.

    Returns:
    None
    """
    try:
        # Create a server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        while True:
            # Accept an incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                # Deserialize the received data
                received_dict = json.loads(data)
                print("Received dictionary:", received_dict)

            # Close the client connection
            client_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()


def send_data(host='localhost', port=12345, data=None):
    """
    Send a serialized dictionary to the server.

    Parameters:
    host (str): The server hostname or IP address to connect to.
    port (int): The server port number to connect to.
    data (dict): The dictionary to send to the server.

    Returns:
    None
    """
    try:
        if data is None:
            data = {'name': 'John Doe', 'age': 30, 'city': 'Anytown'}

        # Create a client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Serialize the dictionary and send it to the server
        serialized_data = json.dumps(data).encode('utf-8')
        client_socket.sendall(serialized_data)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
