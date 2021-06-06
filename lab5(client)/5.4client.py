import socket

s = socket.socket()

s.connect(('192.168.43.38', 8889))

# encryptor
file = open("outputFile.txt", "rb")
SendFile = file.read(1024)

while SendFile:
    data = s.recv(1024)
    print(data)

    s.send(SendFile)
    SendFile = file.read(1024)     

s.close()
