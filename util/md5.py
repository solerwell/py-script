#  coding= utf-8
import hashlib

'generate md5 hex string'


def md5(src):
    """
    user md5 to encrypt data\n
    :param src: source string needed to be encrypted
    :return: the encrypted string

    """
    _md5 = hashlib.md5()
    _md5.update(src.encode("utf-8"))
    return _md5.hexdigest()


if __name__ == "__main__":
    _src = 'B8A9A2D8-48B2-49AB-B119-0C9E05E00DB6'
    _md5_str = md5(_src)
    print(_md5_str)
