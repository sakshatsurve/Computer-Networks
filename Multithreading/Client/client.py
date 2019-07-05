'''

Client Server using multithreading in HTTP Format requests.
Done by Pratik Parekh(801076521) and Sakshat Surve(801080533)

'''

import socket
import sys


def get(conn, filename, hostname):
    request_header = 'GET /{0} HTTP/1.1\r\nHost: {1}\r\n\r\n'.format(filename, hostname).encode('utf-8')
    print('[+] Sending GET/{0} HTTP/1.1 to the Server'.format(filename))
    conn.sendall(request_header)
    response = b''
    while True:
        try:
            recvd = conn.recv(65536)
            if recvd == b'':
                break
        except (socket.error, socket.timeout):
            break
        response += recvd
    conn.close()
    splitted_response = response.split(b'\n\n', 1)
    print('[+] Received: ' + splitted_response[0].decode('utf-8').split('\n')[0])
    response_code = splitted_response[0].decode('utf-8').split(' ')[1]
    if response_code == '200':
        response_payload = splitted_response[1]
        fd = open(filename, 'wb+')
        fd.write(response_payload)
        fd.close()
        print('[+] File {0} downloaded successfully and written to disk'.format(filename))



def put(conn, filename, hostname):
    request_header = 'PUT /{0} HTTP/1.1\r\nHost: {1}\r\n\r\n'.format(filename, hostname).encode('utf-8')
    print('[+] Sending PUT /{0} HTTP/1.1 to the Server'.format(filename))
    try:
        fd = open(filename, 'rb')
        request_payload = fd.read()
        request = request_header + request_payload
        print('[+] Starting upload of the file {0}'.format(filename))
        conn.sendall(request)
        response = b''
        while True:
            try:
                recvd = conn.recv(4096)
                if recvd == b'':
                    break
            except (socket.error, socket.timeout):
                break
            response += recvd
        print('[+] Received: ' + response.decode('utf-8').split('\n')[0])
        fd.close()
    except FileNotFoundError:
        print('[ERROR] File Does not exist')


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    method = sys.argv[3]
    file = sys.argv[4]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print('[+] Connecting to {0} on port {1}'.format(host, str(port)))
        sock.connect((host, port))
        print('[+] Successfully connected to the Server on port {0}'.format(str(port)))
    except socket.error:
        print('[ERROR] Cannot connect to the Server. Exiting.')
        sys.exit(1)
    if method == 'GET':
        get(sock, file, host)
    elif method == 'PUT':
        put(sock, file, host)
    else:
        print('[ERROR] Invalid Request Method. Please choose between GET and PUT.')
    sock.close()
