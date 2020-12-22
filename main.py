import socket, ssl
from struct import *
hsmSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(hsmSocket,
                           keyfile="server.key",
                           certfile="server.crt",
                           server_side=False,
                           ca_certs=None,
                           cert_reqs=ssl.PROTOCOL_SSLv23,
                           do_handshake_on_connect=True,
                           suppress_ragged_eofs=True,
                           ciphers="ECDHE-RSA-AES128-GCM-SHA256"
                           )

HOST = 'hopdev.first-tech.net' #'hopdev.first-tech.net' #'hop.first-tech.net' #'129.151.32.241'
HOST_PORT = 443
BUFFER_SIZE = 1024

# paste command example within inverted commas below:
COMMAND = '0000NO00'

try:
    ssl_sock.connect((HOST, HOST_PORT))

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

    print "sent data (ASCII) : ", MESSAGE
    print "sent data (HEX) : ", MESSAGE.encode('hex')
    print "-------------------------------------------"
    print "received data (ASCII): ", data
    print "received data (HEX) : ", data.encode('hex')
    pass
except:
    print "Connection Lost"

print "Send Finish"