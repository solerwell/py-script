# codding= utf-8

"""test file related method"""

if __name__ == '__main__':
    _src_path = 'C:\\Users\\soler\\Desktop\\项目\\易品3.7.0数据项增加md5\\test-data\\idfa-tiny.txt'
    _dest_path = 'C:\\Users\\soler\\Desktop\\项目\\易品3.7.0数据项增加md5\\test-data\\idfa-tiny_md5.txt'
    print("===main program begin...")
    with open(_dest_path, 'w+') as _dest:
        with open(_src_path, 'r') as _src:
            for line in _src.readlines():
                print(line.strip())
                _dest.write(line)
