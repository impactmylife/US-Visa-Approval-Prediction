from us-visa.logger import logging
from us-visa.exceptions import USvisaException
import sys

try:
    a = 1/"10"
except Exception as e:
    raise USvisaException(e, sys) from e