from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    cliecntSocket.connect((mailserver,port))

    recv = clientSocket.recv(1024).decode()
    
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
