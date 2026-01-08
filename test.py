import random
import string
kode_buku = ''.join(random.choice(string.ascii_letters.upper()) for i in range(6))
print(kode_buku)