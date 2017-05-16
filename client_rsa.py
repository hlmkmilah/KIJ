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
        print p
        break
for i in range (2,randomaja) :  # menentukan nilai prima q dan nilai q dirahasiakan
    q = random.randint(2,randomaja)
    prima = True
    for j in range (2,q) :
        if(q%j==0) : prima = False

    if(prima == True):
        print q
        break
n = p*q # nilai n tidak dirahasiakan
print  n

m = (p-1)*(q-1) # nilai m perlu dirahasiakan
print m

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
print x

# mencari kunci privat (d) 
for j in range(3, m, 2):
    if j * x % m == 1:
        d = j
        break

print d


kunci_public = [x,n]
print kunci_public
kunci_privat = [d,n] 
print kunci_privat
#-----------------------simpan txt----------------------------
with open('kuncipublik_client.txt', 'wb') as file:
    file.write("%d,%d" % (x, n))

while True:
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 11000)
        #print >> sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)
        # Send data
        message = raw_input('Client ngomong : ')
        with open ('kuncipublik_server.txt', 'rb') as kpb:
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
        print enkripsi
        print >>sys.stderr, 'sending "%s"' % enkripsi
        sock.send(kirim)
  
        data = sock.recv(4096)
        terima = pickle.loads(data)
        print terima
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




    finally:
        sock.close()