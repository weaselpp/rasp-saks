#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 NXEZ.COM.
# http://www.nxez.com
#





#import sys
#sys.path.append('/usr/src/python/SAKS20')

import saksconfig
saksconfig.importLibPath()

from sakshat import SAKSHAT
import time
from datetime import datetime
from sakspins import SAKSPins as PINS
# import traceback
import random

#Declare the SAKS Board
SAKS = SAKSHAT()

if __name__ == "__main__":
    SAKS.saks_gpio_reset()
    
