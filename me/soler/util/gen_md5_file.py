# codding= utf-8
from me.soler.util import md5
import logging

"transfer to md5 string form src file by line"


def transfer_to_md5(src_file_path, dest_path):
    """
    transfer the file to md5-encrypted-data line by line
    :param src_file_path: the raw data file path
    :param dest_path: destination file path
    :return: the md5-encrypted-data
    """
    if (not src_file_path) or (not dest_path):
        print("===the file path is must not none!")
        return
    try:
        with open(dest_path, 'w+') as _dest_file:
            with open(src_file_path, 'r') as _src_file:
                # return content line array
                for line in _src_file.readlines():
                    md5_str = md5.md5(line.strip())
                    _dest_file.write(md5_str + "\n")

    except BaseException as be:
        logging.error("transfer md5 data error", be)
        raise


if __name__ == '__main__':
    _src_path = 'C:\\Users\\soler\\Desktop\\项目\\易品3.7.0数据项增加md5\\test-data\\idfa-tiny.txt'
    _dest_path = 'C:\\Users\\soler\\Desktop\\项目\\易品3.7.0数据项增加md5\\test-data\\idfa-tiny_md5.txt'
    print("===main program begin...")
    transfer_to_md5(_src_path, _dest_path)
