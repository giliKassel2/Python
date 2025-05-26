import datetime


def run_time(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        return end - start
    return inner

@run_time
def sum():
    sumi = 0
    for i in range(1000):
        sumi += i

print(sum())

dic ={}
def cache(fibunachi):
    def inner(n):
        if dic.keys().__contains__(n):
            return dic[n]
        else:
            dic[n] = fibunachi(n)
            return dic[n]
    return inner
@run_time
@cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(80))




print(fib(80))