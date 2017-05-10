# RSA
#### Rivest, Shamir, Adleman
Pada bidang kriptografi adalah sebuah algoritma pada enkripsi public key, namun kunci yang digunakan untuk enkripsi maupun dekripsi berbeda.
Merupakan algortima pertama yang cocok untuk _digital signature_. Kekuatan utama dari RSA adalah kesulitan dalam memfaktorkan bilangan yang besar (NP Hard Problem),
sehingga dapat dimanfaatkan untuk mengamankan data.
### Langkah-langkah dalam mengenkripsi atau mengdekripsi RSA adalah sebagai berikut :
1. Pilih 2 buah bilangan prima p dan q.
2. Hitung nilai n = p * q , (usahakan agar setidaknya n > 255 agar dapat mewakili seluruh karakter ASCII).
3. Hitung nilai m = (p-1) * (q-1).
4. Cari nilai e , dimana e merupakan relatif prima dari m.
5. Cari nilai d , yang memenuhi persamaan ed ≡ 1 mod m atau d = e-1 mod m.
6. Kunci public (e , n) dan kunci private (d , n).
7. Fungsi enkripsi → E (ta)=tae mod n ; dimana ta merupakan karakter ke-a dari message (pesan) yang akan dienkripsi.
8. Fungsi dekripsi → D (ca)=cad mod n ; dimana ca merupakan karakter ke-a dari ciphertext yang akan didekripsikan.
#
Pada _public key_ terdiri atas:
- _N_, modulus yang digunakan.
- _e_, eksponen publik.
#
Pada _private key_ terdiri atas:
- _N_, modulus yang digunakan, digunakan pula pada _public key_.
- _d_, eksponen pribadi(sering juga disebut eksponen dekripsi), yang harus dijaga kerahasiaannya.
#
Biasanya, berbeda dari bentuk _private key_(termasuk parameter CRT):
- _p_ dan _q_, bilangan prima dari pembangkitan kunci.
- _d mod (p-1)_ dan _d mod (q-1)_ (dikenal sebagai _dmp1_ dan _dmq1_).
- _(1/q) mod p_ (dikenal sebagai _iqmp_).
#
Proses enkripsi pesan:

Misalkan Bob ingin mengirim pesan **m** ke Alice. Bob mengubah **m** menjadi angka **n < N**,
menggunakan protokol yang sebelumnya telah disepakati dan dikenal sebagai _padding scheme_.
Maka Bob memiliki **n** dan mengetahui **N dan e**, yang telah diumumkan oleh Alice.

Bob kemudian menghitung ciphertext **c** yang terkait pada n:

**c = n^e mod N**

Perhitungan tersebut dapat diselesaikan dengan cepat menggunakan metode exponentiation by squaring. Bob kemudian mengirimkan c kepada Alice.
#
Proses dekripsi pesan:

Alice menerima c dari Bob, dan mengetahui private key yang digunakan oleh Alice sendiri. Alice kemudian memulihkan n dari c dengan langkah-langkah berikut:

**n = c^d mod N**

Perhitungan di atas akan menghasilkan n, dengan begitu Alice dapat mengembalikan pesan semula m. Prosedur dekripsi bekerja karena

**c^d ≡ (n^(e))^d ≡ n^(ed) (mod N)**

Kemudian, dikarenakan ed ≡ 1 (mod p-1) dan ed ≡ 1 (mod q-1), hasil dari _Fermat's little theorem_.

**n^(ed) ≡ n (mod p)**

dan

**n^(ed) ≡ n (mod q)**

Dikarenakan p dan q merupakan bilangan prima yang berbeda, mengaplikasikan Chinese Remainder Theorem akan menghasilkan dua macam kongruen

**n^(ed) ≡ n (mod pq)**

serta

**c^d ≡ n (mod N)**

###### Referensi:
###### - PPT KIJ Network Security Pak Tohari
###### - https://id.wikipedia.org/wiki/RSA
###### - http://octarapribadi.blogspot.co.id/2016/02/enkripsi-dan-dekripsi-menggunakan-rsa.html
