__all__ = [
    'get_version'
]

from typing import Tuple as __Tuple

from mypackage.__version__ import __author__
from mypackage.__version__ import __author_email__
from mypackage.__version__ import __license__
from mypackage.__version__ import __version__
from mypackage.__version__ import VERSION as __VERSION

from mypackage import models
#from mypackage._mypackage import my_function



def get_version() -> __Tuple[int]:
    return __VERSION
