import socket
from tests_server import a, b

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket family
    server.bind(('127.0.0.1', 2001))
    print('Working...')
    # server = socket.create_server(('127.0.0.1', 2001))  # analog of the code above

    server.listen(4)  # server listen different asks and how many asks in the order
    client_socket, address = server.accept()
    data = client_socket.recv(1024).decode(('utf-8')) # decode to UTF-8
    print(data)

    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'  # info for some browsers about type of answer (encoding headlines)
    content = 'Well done!'.encode('utf-8')
    client_socket.send(HDRS.encode('utf-8') + content)  # send answer

    print('Okey-okey')


def load_some_answer(request_data):
    path = request_data.split(' ')[1]
    responce = ''
    # with open()

'https://www.youtube.com/watch?v=bA-L87QZtic&t=2s'
