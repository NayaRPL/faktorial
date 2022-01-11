print("mencari faktorisasi bilangan prima")
print("menggunakan cara perulangan")
angka=int(input("masukkan angka:"))
faktorial=1
for i in range(1,angka+1):
    faktorial*=i
    print(faktorial)


n = int(input('Masukkan nilai n: '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')

print("mengguanakan rekursif")
a=int(input("masukkan hasil:"))

def hitung_faktorial(a):
    if a >2:
        return a * hitung_faktorial(a-1)
    return 2

faktorial=hitung_faktorial(a)
print(f'{n}! = {faktorial}')


    
    
    



    
