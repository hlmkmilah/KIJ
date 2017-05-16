import socket
import sys
import math
import pickle
import random

randomaja = int(raw_input('Masukkan angka terserah: '))    #range nilai untuk menentukan random nilai p dan q
k = 0
prim = []
for i in range (2,randomaja) :  # menentukan nilai prima p dan nilai p dirahasiakan
    p = random.randint(2,randomaja)
    prima = True
    for j in range (2,p) :
        if(p%j==0) : prima = False

    if(prima== True):
        print "nilai prima p = ", p
        break
for i in range (2,randomaja) :  # menentukan nilai prima q dan nilai q dirahasiakan
    q = random.randint(2,randomaja)
    prima = True
    for j in range (2,q) :
        if(q%j==0) : prima = False

    if(prima == True):
        print "nilai prima q =", q
        break
n = p*q # nilai n tidak dirahasiakan
print "p x q =",  n

m = (p-1)*(q-1) # nilai m perlu dirahasiakan
print "(p-1) x (q-1) = ", m

# mencari faktor terbesar
def gcd(a, b):
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True

x = 0
# memilih kunci publik (e) yang relatif prima terhadap m
for i in range(3, m, 2):
    i = random.randint(3,m)
    if gcd(i, m) == 1:
        x = i
        break
# print x

# mencari kunci privat (d) 
for j in range(3, m, 2):
    if j * x % m == 1:
        d = j
        break
# print d

kunci_public = [x,n]
print "Kunci Publik = ", kunci_public
kunci_privat = [d,n] 
print "Kunci Privat = ", kunci_privat
#-----------------------simpan txt----------------------------
with open('kuncipublik_server.txt', 'wb') as file:
    file.write("%d,%d" % (x, n))


server_address = ('localhost', 11000)
print >> sys.stderr, 'starting up on %s port %s' % server_address

# Listen for incoming connections
while True:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(server_address)
    sock.listen(1)

    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096)
            terima = pickle.loads(data)
            print >>sys.stderr, 'received "%s"' % terima
            
            dekrip = []
            dekrip2 = []
            
            j = 0
            fix = map(int, terima)
            while j < len(terima):
                dekrip.append(((fix[j]) ** d) % n)
                j+=1
            print dekrip

            plain = [chr(char) for char in dekrip]
            plaintext = ''.join(plain)
            print plaintext               

            if data:
                message = raw_input('Server ngomong : ')
                with open ('kuncipublik_client.txt', 'rb') as kpb:
                    kp = kpb.read()
                e = int(kp.split(',')[0])
                print e
                n2 = int(kp.split(',')[1])
                print n2
                s=list(message)
                print s
                l = [ord(c) for c in s]
                enkrip = []
                enkrip2 = []
                print l
                i = 0
                while i < len(message):
                    enkrip.append((l[i] ** e) % n2)
                    i+=1
                i=0
                while i < len(message):
                    enkrip2.append(str(enkrip[i]))
                    i+=1
                # kirim = pickle.dumps(enkrip)
                print enkrip
                print enkrip2
                kirim = pickle.dumps(enkrip)
                enkripsi = ''.join(map(str,enkrip))
                print >> sys.stderr, 'sending "%s"' % enkripsi
                #print >>sys.stderr, 'sending data back to the client'
                connection.sendall(kirim)
            else:
                print >>sys.stderr, 'no more data from', client_address
            break
    finally:
        # Clean up the connection
        connection.close()