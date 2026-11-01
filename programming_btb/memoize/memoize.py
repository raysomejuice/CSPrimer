import urllib.request


def memoize(function):
    cache = {}
    def memo_wrapper(x):
        if x in cache:
            return cache[x]
        cache[x] = function(x)
        return cache[x]
    return memo_wrapper


@memoize
def fetch(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content


@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fetch('http://google.com')[:80])
    print(fib(800))
