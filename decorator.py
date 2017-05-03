from time import ctime


def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called'%(ctime(),func.__name__))
        return func()
    return wrappedFunc()
def test():
    print(11111)
def main():
    return test()
@tsfunc
def foo():
    pass
if __name__ == '__main__':
    main()


