import sys

is_PY2 = sys.version_info < (3, 0)

if is_PY2:
    from ConfigParser import ConfigParser
    b = lambda x: x
    s = lambda x: x
else:
    from configparser import ConfigParser
    b = lambda x: bytes(x, "utf-8")
    s = lambda x: str(x, "utf-8")
