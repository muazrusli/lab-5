import socket

s = socket.socket()
print("Berjaya cipta socket")


s.bind(('',8889))
print("Berjaya bind socket di port: "+str(8889))

s.listen(5)
print("Socket sedang menunggu client!")

file = open("inputfile.txt","wb") 

while True:
    c, addr = s.accept()
    print("connect dari: "+str(addr))
    c.send(b'Mekacih awak !')

    RecvFile = c.recv(1024)
    while RecvFile:
        file.write(RecvFile)
        RecvFile = c.recv(1024)
    file.close()
    print("\n File berjaya mendapat salinan file \n")

    c.close()
    break
