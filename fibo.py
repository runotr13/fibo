def fib(sayi):
  a=1
  b=1
  fibo = [a,b]
  for i in range(sayi):
    a,b = b,a+b
    fibo.append(b)
  print(fibo)
fib(8)
