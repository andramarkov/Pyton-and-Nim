
import nimporter
import montenimpy
import time

start_nim = time.time()
print('pi: ',montenimpy.approxpi(100000000),' in: ', time.time() - start_nim)








'''
start_nim = time.time()
montenimpy.approxpi(100000000)
end_nim = time.time()

print('Durasi: {:.2f}'.format(end_nim - start_nim))
print('pi: ',approxpi(100000000),' in: ', time.time() - start)
'''