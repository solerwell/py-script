import sys
from os.path import join, dirname, abspath


def do_import():
    """

    :return:
    """
    _top_dir = abspath(join(dirname(__file__)))
    print("_top_dir: " + _top_dir)
    sys.path.append(_top_dir)
