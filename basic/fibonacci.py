#encoding=utf-8
a = 0
b = 1
def fib():
    global a
    global b
    a,b = b,a+b
    yield a

N = input("please input fibonacci number:")

for i in range(int(N)):
    f = fib()
    print(next(f), end=' ')
print()
