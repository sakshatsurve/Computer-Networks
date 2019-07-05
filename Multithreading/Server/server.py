'''

Client Server using multithreading in HTTP Format requests.
Done by Pratik Parekh(801076521) and Sakshat Surve(801080533)

'''

import socket
from sys import exit, argv
import threading
import time
from pathlib import Path


#error functiton for Internal Server Error
def error_500(conn):
    error_response = "HTTP/1.1 400 Internal Server Error\nConnection: close\n\n<html><body><center><h3>Error 500: " \
                     "Internal Server Error</h3></center></body></html>".encode('utf-8')
    conn.sendall(error_response)
    print('[+] Returned 500 to {0}'.format(conn.getsockname()))

#error functiton for a Bad Request
def error_400(conn):
    error_response = "HTTP/1.1 400 Bad Request\n\n<html><body><center><h3>Error 400: Bad " \
                     "Request</h3></center></body></html>".encode('utf-8')
    conn.sendall(error_response)
    print('[+] Returned 400 to {0}'.format(conn.getsockname()))


#error functiton for File not found
def error_404(conn):
    error_response = "HTTP/1.1 404 Not Found\nConnection: close\n\n<html><body><center><h3>Error 404: File Not " \
                     "Found</h3></center></body></html>".encode('utf-8')
    conn.sendall(error_response)
    print('[+] Returned 404 to {0}'.format(conn.getsockname()))


#Response message if the file is overwritten
def ok_200(conn, response_data):
    header = b'HTTP/1.1 200 OK\n'
    time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    header += 'Date: {now}\n'.format(now=time_now).encode('utf-8')
    header += b'Server: Python HTTP Server\n'
    header += b'Connection: close\n\n'  # Signal that connection will be closed after completing the request
    response = header + response_data
    conn.sendall(response)
    print('[+] Returned 200 to {0}'.format(conn.getsockname()))


#Response message for ne file created
def ok_201(conn, fn):
    header = b'HTTP/1.1 201 Created\n'
    time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    header += 'Content-Location: {0}\n'.format(fn).encode('utf-8')
    header += 'Date: {now}\n'.format(now=time_now).encode('utf-8')
    header += b'Server: Python HTTP Server\n'
    header += b'Connection: close\n\n'  # Signal that connection will be closed after completing the request
    response = header
    conn.sendall(response)
    print('[+] Returned 201 to {0}'.format(conn.getsockname()))

#Function to handle the PUT command
def put_handler(conn, filename, payload):
    print('[+] PUT {0} HTTP/1.1 from {1}'.format(filename, conn.getsockname()))
    is_exists = Path(filename[1:]).is_file() # is_file returns a boolean if the file already exists in the same folder.
    try:
        fd = open(filename[1:], 'wb+') #starting from 1 to avoid the '/'
        fd.write(payload)
        fd.close()
        ok_200(conn, b'') if is_exists else ok_201(conn, filename) #if the file is present then message response 200
                                                                   #otherwise message response 201
    except (IOError, OSError):
        error_500(conn)

#Function to handle the GET command
def get_handler(conn, filename):
    print('[+] GET {0} HTTP/1.1 from {1}'.format(filename, conn.getsockname()))
    if filename == '/':
        filename = 'index.html'           #if no file is passed then it uses index.html as the default command
    else:
        filename = filename[1:]           #else it discards the '/' and saves the filename
    try:
        fd = open(filename, 'rb')
        ok_200(conn, fd.read())
        fd.close()
    except FileNotFoundError:
        error_404(conn)


def client_handler(connection, address):
    time.sleep(30)  #Enable this to see that multithreading is working
    print('[+] New connection from {0}'.format(address))
    request = b""
    connection.settimeout(1.0)
    while True:
        try:
            data = connection.recv(4096)
        except socket.timeout:
            break
        if not data:
            break
        request += data
    str_list = request.split(b' ', 2)
    method = str_list[0].decode('utf-8')
    if method == 'PUT':
        payload = request.split(b'\r\n\r\n')[1]
        put_handler(connection, str_list[1].decode('utf-8'), payload)
    elif method == 'GET':
        get_handler(connection, str_list[1].decode('utf-8'))
    else:
        error_400(connection)
    connection.close()


def serve(listen_on, port):
    print('Attempting to start server on port {0}'.format(str(port)))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = (listen_on, port)
    try:
        sock.bind(server)
        sock.listen(5)
    except socket.error:
        print('[ERROR] Cannot start server')
        exit(1)
    print('[+] Server started on port {0}. Waiting for clients to connect...'.format(str(port)))
    while True:
        try:
            client, addr = sock.accept()
            t = threading.Thread(target=client_handler, args=(client, addr))
            t.start()
        except (KeyboardInterrupt):
            if client:
                client.close()
            break

if __name__ == '__main__':
    serve('localhost', int(argv[1]))
