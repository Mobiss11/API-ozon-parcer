import time

from module_first import module_first
from module_second import module_second
from consts import MESSAGE_LOG_START, MESSAGE_LOG_WAITING

while True:

    print(MESSAGE_LOG_START)

    module_first()
    module_second()

    print(MESSAGE_LOG_WAITING)

    seconds_waiting = 86400 - 2760
    time.sleep(seconds_waiting)
