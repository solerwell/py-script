# codding= utf-8
import sys
import logging

# let python find the module of this project
sys.path.append('D:\\workspace\\py_script')

from me.soler.util import md5

"""transfer to md5 string form src file by line"""


def transfer_to_md5(src_file_path, dest_path):
    """
    transfer the file to md5-encrypted-data line by line\n
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
        logging.error("transfer md5 data error" + be)
        raise


# the main function has two args (.etc using windows cmd to execute this program)
# 1st:  the source file path
# 2nd:  the destination file path
if __name__ == '__main__':
    if sys.argv.__len__() < 3:
        raise ValueError("the function's arg is not complete!")
    _arg_count = 0
    for arg in sys.argv:
        print("arg_count= " + str(_arg_count) + "\targ= " + str(arg))
        _arg_count = _arg_count + 1
    _src_path = sys.argv[1]
    _dest_path = sys.argv[2]
    print("===main program begin...")
    transfer_to_md5(_src_path, _dest_path)
