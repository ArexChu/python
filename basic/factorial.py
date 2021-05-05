#encoding=utf-8

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
fact = fact(6)
print(fact)
