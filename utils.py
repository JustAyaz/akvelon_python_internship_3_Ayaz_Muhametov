# i couldn't understand how to show usages of this func,
# but u can check this out http://www.hintfox.com/article/chisla-fibonachchi-prakticheskoe-primenenie.html
from functools import lru_cache


# Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls.
# https://docs.python.org/dev/library/functools.html#functools.lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(12))
