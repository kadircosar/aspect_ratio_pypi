from aspect_ratio_kd import __version__
from aspect_ratio_kd.get_version import upgrade_version

def test_version():
    assert __version__ == '0.1.1'


def get_version():
    return upgrade_version