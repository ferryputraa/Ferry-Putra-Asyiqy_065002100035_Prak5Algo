print("-------DERET FIBONACII-------")
n, a, b=(
  int(input("Masukkan jumlah bilangan  : ")),
  int(input("Masukkan bilangan pertama : ")),
  int(input("Masukkan bilangan kedua   : ")))
for i in range(n):
  print(a)
  c=b+a
  a=b
  b=c
