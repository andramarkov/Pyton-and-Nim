#Nim, as fast as C, as expressive as Python
Beberapa waktu belakangan ini, lagi suka eksplorasi bahasa pemrograman yang 'jarang' di cari, setidaknya jika mengacu pada posting lowongan pekerjaan di job portal lokal.

Salah satu yang menarik perhatian saya adalah Nim yang sangat mirip dengan Python, menurut berbagai review, program yang di tulis dengan Nim ini sangat cepat bahkan (katanya) bisa mendekati bahkan setara eksekusi program yang di tulis dengan C.

Sebenarnya sebagai compiled languange tentunya eksekusi Nim sudah seyogyanya lebih cepat dari Python yang interpreted.

Saya mencoba hitungan sederhana approksimasi nilai pi dengan Monte Carlo Method (n = 100.000.000), hasilnya Nim sekitar 80 kali lebih cepat di banding Python.

##Hasil percobaan:
###1. Python (tidak di optimasi)
Waktu eksekusi sekitar 56 detik

<img src="/python/py.png"
     alt="python"
     style="float: left; margin-right: 10px;" />

###2. Python dengan Numpy
Dengan bantuan Numpy, eksekusi menjadi jauh lebih cepat, sekitar 3.8 detik

<img src="/python/py+numpy.png"
     alt="python and numpy"
     style="float: left; margin-right: 10px;" />

###3. Nim
Perhatikan kode nya yang sangat mirip dengan Python, waktu eksekusi sekitar 0.7 detik (flag = --gc:refc --passC:"-flto" -d:release)

<img src="/nim/nim.png"
     alt="nim"
     style="float: left; margin-right: 10px;" />

###4. Python dengan Nimpy dan Nimporter 
Ini sangat menarik karena memungkinkan integrasi bidireksional antara Python <-> Nim, ini memungkinkan kita untuk 'memanggil' library python seperti Pandas dan Numpy dari Nim, begitu juga sebaliknya 'memanggil' modul yang di tulis dengan Nim dari Python.

Untuk percobaan kali ini, skrip Python kita akan menyerahkan 'heavy lifting' approksimasi nilai pi kepada Nim, caranya sbb:

Di Nim kita import nimpy lalu menambahkan pragma {.exportpy.}

namafile: montenimpy.nim
```
import math
import random 
import nimpy

randomize()
proc approxpi(nthrows: float): float {.exportpy.} =
  var inside = 0.0
  for i in 1..int64(nthrows):
    if hypot(rand(1.0), rand(1.0)) <= 1:
      inside += 1
  result = 4 * inside / nthrows
```

Di Python kita import nimporter dan file nim di atas

namafile: app.py
```
import nimporter
import montenimpy
import time

start_nim = time.time()
print('pi: ',montenimpy.approxpi(100000000),' in: ', time.time() - start_nim)
```

Jalankan dengan perintah `python app.py`

<img src="/pytho+nim/py+nim.png"
     alt="python and nim"
     style="float: left; margin-right: 10px;" />

Waktu eksekusi sekitar 1.25 detik, walaupun tidak secepat native nim (0.7x detik) tetapi tetap lebih cepat di banding Python + Numpy (3.8 detik)

###Spesifikasi:
Prosesor: Intel Core i5-3437U
RAM: 8GB
OS: MacOS Catalina 10.15.7
Python: 3.9.4
Nim: 1.6.4