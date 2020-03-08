import time


class Common(object):

    @classmethod
    def uid(cls):
        s = str(time.time())[6:10]
        return s


if __name__ == '__main__':
    print(Common.uid())