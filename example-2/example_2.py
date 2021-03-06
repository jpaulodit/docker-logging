"""
The sample code writes log messages to SYSLOG.

"""

import logging
import sys
import time

from logging.handlers import SysLogHandler


formatter = logging.Formatter('%(asctime)-15s %(name)-12s: %(levelname)-8s %(message)s')

logger = logging.getLogger('to.syslog.example2')
handler = SysLogHandler(address='/dev/log')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

while True:
    logger.debug('Logging a debug statement into syslog.')
    logger.error('Logging an error statement into syslog.')
    time.sleep(2)
