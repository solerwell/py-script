# codding= utf-8
import sys
from os.path import join, dirname, abspath


def do_import():
    """
        import all sub-package and submodule of the project.
        this py file must be located in the root directory
    """
    _top_dir = abspath(join(dirname(__file__)))
    print("_top_dir: " + _top_dir)
    sys.path.append(_top_dir)
