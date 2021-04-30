#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - cologler <skyoflw@gmail.com>
# ----------
# parse number style datetime between (1970, 2050)
# ----------

from typing import *
from datetime import datetime, timedelta

CONST_MIN_YEAR = 1970
CONST_MAX_YEAR = 2050

class _TimeStyle:
    def match(self, value: float) -> bool:
        raise NotImplementedError

    def to_datetime(self, value: float) -> datetime:
        raise NotImplementedError

    def from_datetime(self, dt: datetime) -> float:
        raise NotImplementedError


class _UnixTimestamp(_TimeStyle):
    DT1970 = datetime(1970, 1, 1)
    MIN = 0
    MAX = (datetime(CONST_MAX_YEAR, 12, 31) - DT1970).days * 24 * 60 * 60

    def __init__(self, precision) -> None:
        self._resolution = precision
        self.max = self.MAX * precision
        self.min = self.MIN

    def match(self, value: float):
        return self.min < value < self.max

    def to_datetime(self, value: float) -> datetime:
        if self._resolution == 1: # seconds
            delta = timedelta(seconds=value)
        elif self._resolution == 10**3: # milliseconds
            delta = timedelta(milliseconds=value)
        elif self._resolution == 10**6: # microseconds
            delta = timedelta(microseconds=value)
        else:
            delta = timedelta(microseconds=value*(self._resolution/1000/1000))
        return self.DT1970 + delta

    def from_datetime(self, dt: datetime) -> float:
        delta = dt - self.DT1970
        return ((delta.days * 86400 + delta.seconds) * 10**6 + delta.microseconds) * (self._resolution/1000/1000)

    def __str__(self):
        s = 'days_after(1970) * 60 * 60 * 24'
        if self._resolution > 1:
            s += f' * {self._resolution}'
        return s


_STYLES = (
    _UnixTimestamp(1),      # seconds
    _UnixTimestamp(10**3),  # milliseconds
    _UnixTimestamp(10**6),  # microseconds
    _UnixTimestamp(10**9),  # nanoseconds
)

def infer_style(value: float) -> Optional[_TimeStyle]:
    'infer datetime style from a float value.'
    for style in _STYLES:
        if style.match(value):
            return style

def parse(value: float) -> Optional[datetime]:
    'parse datetime from a float value.'
    s = infer_style(value)
    return s.to_datetime(value) if s else None
