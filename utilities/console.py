# -*- coding: utf-8 -*-

#    Copyright (C) 2014-2015 by
#    Colin Dablain <colin.dablain@gmail.com>
#    All rights reserved.
#    Licensed under GNU GPL v3; see license.txt
# Code adapted from http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python

def getTerminalSize():
    """
    Returns the terminal's size in (width, height) form
    """
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])
