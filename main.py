#coding: utf-8
import socket, ssl, datetime
from struct import *

start_time = datetime.datetime.now()

# NUMBER INTERACTIONS OF THE TEST
N_TESTS = 100

HOST = 'HOST_DA_APLICAÇÃO' # host da aplicacao
# HOST = '10.20.60.160'
HOST_PORT = 1540
BUFFER_SIZE = 1024

# paste command example within inverted commas below:
COMMAND = '0000NO00'

# loop para stress test
for item in range(N_TESTS):
    hsmSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ssl_sock = hsmSocket
    ssl_sock = ssl.wrap_socket(hsmSocket)
    try:
        ssl_sock.connect((HOST, HOST_PORT))
        print "========================================================================================================"
        print "Connection OK"

        # 1st two bytes must be command length
        SIZE = pack('>h', len(COMMAND))

        # join everything together
        MESSAGE = SIZE + COMMAND

        # send MESSAGE
        ssl_sock.send(MESSAGE)

        # receive
        data = ssl_sock.recv(BUFFER_SIZE)

        # close socket
        ssl_sock.close()
        print "********************************************************************************************************"
        print "Teste Numero : ", item + 1
        print "sent data (ASCII) : ", MESSAGE
        print "sent data (HEX) : ", MESSAGE.encode('hex')
        print "received data (ASCII): ", data
        print "received data (HEX) : ", data.encode('hex')
        pass
    except:
        print "Connection Lost"
    print "********************************************************************************************************"
    print "Finish Command"

current_time = datetime.datetime.now()
elapsed_time = current_time - start_time
print "--------------------------------------------------------------------------------------------------------"
print "Host : ", HOST
print "Port : ", HOST_PORT
print "Finish Test : ", elapsed_time
