import os



libPath = '/home/pi/.src/python/SAKS20'

def importLibPath():
    execStr = ('import sys\nsys.path.append("%s")' % (libPath))
    # print(execStr)
    exec(execStr)






