#  coding= utf-8
import hashlib


def md5(src):
    _md5 = hashlib.md5()
    _md5.update(src.encode("utf-8"))
    return _md5.hexdigest()


if __name__ == "__main__":
    _src = '123456'
    _md5_str = md5(_src)
    print(_md5_str)
