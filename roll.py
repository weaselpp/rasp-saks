#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 NXEZ.COM.
# http://www.nxez.com
#

import saksconfig
# sys.path.append('/usr/src/python/SAKS20')
saksconfig.importLibPath()


from sakshat import SAKSHAT
import time
from datetime import datetime
from sakspins import SAKSPins as PINS
# import traceback
import random

#Declare the SAKS Board
SAKS = SAKSHAT()

__start_time = datetime.utcnow()
__end_time = datetime.utcnow()
__running = False

def tact_event_handler(pin, status):
    '''
    called while the status of tacts changed
    :param pin: pin number which stauts of tact is changed
    :param status: current status
    :return: void
    '''
    global __start_time
    global __end_time
    global __running
    # print(traceback.print_stack())
    # print("pin: " + str(pin) + " status: " + str(status) + str(type(status)))

    if pin == PINS.TACT_RIGHT:
        if status == True:
            SAKS.digital_display.show(("%04d" % (random.randint(1, 100))))
            __running = True
        else:
            __running = False

if __name__ == "__main__":
    SAKS.tact_event_handler = tact_event_handler
    SAKS.digital_display.show(("%04d" % (0)))
    while True:
        if __running:
            SAKS.digital_display.show(("%04d" % (random.randint(1, 100))))

        time.sleep(0.0001)
    input("Enter any keys to exit...")
