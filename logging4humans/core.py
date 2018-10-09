# -*- coding: utf-8 -*-
"""
 Logging4Humans
 - Author:      Daniel J. Umpierrez
 - Created:     09-10-2018
 - License:     MIT
"""
import collections
import collections as col
import datetime as dt

import term

term.gray = term.white + term.dim

wLn = term.writeLine
fmt = term.format

white = term.white
dim = term.dim
bold = term.bold
cyan = term.cyan
yellow = term.yellow
red = term.red
gray = term.gray

__all__ = ['Logger']

COLORS = [gray]


class Level:
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    VERBOSE = 'VERBOSE'
    CRITICAL = 'CRITICAL'

    NAMES = [DEBUG, VERBOSE, INFO, WARN, ERROR, CRITICAL]
    STYLES = [(gray,), (white,), (cyan,), (bold, yellow), (red,), (red, bold)]
    VALUES = [v * 10 for v in range(len(NAMES))]

    DICT = collections.OrderedDict(zip(NAMES, VALUES))

    @classmethod
    def get(cls, v, get_style=False):
        """
        Returns level value, name or style depending of the "v" supplied value type.

        Return level name if "v" value is int type level name will be returned.

        :param v:
        :param get_style:
        :return:
        """
        if v is not None:
            if isinstance(v, int) and v in cls.VALUES:
                return cls.STYLES[v // 10] if get_style else cls.NAMES[v // 10]
            elif isinstance(v, str) and v.upper() in cls.NAMES:
                idx = cls.NAMES.index(v.upper())
                return cls.STYLES[idx] if get_style else idx * 10


class Logger:
    """
    Log made simple.

    >>> log = Logger('test', 'info')
    """

    _datefmt = '[{:%b-%d %H:%M:%S}]'
    _name = 'Log'
    _fmt = '{}[{}][{}] {}'

    def _get_datetime(self):
        return self._datefmt.format(dt.datetime.utcnow())

    def __init__(self, name, level=None, max_history=1000):

        if str(level).upper() in Level.NAMES:
            self._level = str(level).upper()
        elif level and isinstance(level, int) and level in Level.VALUES:
            self._level = Level.get(level)
        else:
            self._level = Level.INFO

        self._name = str(name or '')
        self._history = col.deque(maxlen=max_history)

    def _echo(self, msg, color=None):
        txt = self._fmt.format(self._get_datetime(), self._name, self._level, msg)
        wLn(txt, *color) if color else print(txt)

    def debug(self, msg):
        if Level.get(self._level) == 0:
            self._echo(msg, Level.get(0, True))

    def verbose(self, msg):
        if Level.get(self._level) <= 10:
            self._echo( msg, Level.get(10, True))

    def info(self, msg):
        if Level.get(self._level) <= 20:
            self._echo(msg, Level.get(20, True))

    def warning(self, msg):
        if Level.get(self._level) <= 30:
            self._echo(msg, Level.get(30, True))

    def error(self, msg):
        if Level.get(self._level) <= 40:
            self._echo(msg, Level.get(40, True))

    def critical(self, msg):
        if Level.get(self._level) == 50:
            self._echo(msg, Level.get(50, True))

    warn = warning
    w = warning
    d = debug
    i = info
    e = error
    c = critical
    v = verbose
