import importlib
import importlib.util
from typing import Union, Text

from pyms.exceptions import PackageNotExists


def import_from(module: Text, name: Text):

    module = __import__(module, fromlist=[name])
    return getattr(module, name)


def import_package(package: Text):
    return importlib.import_module(package)


def check_package_exists(package_name: Text) -> Union[Exception, bool]:
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        raise PackageNotExists("{package} is not installed. try with pip install -U {package}".format(package=package_name))
    return True
