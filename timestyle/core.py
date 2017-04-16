#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - cologler <skyoflw@gmail.com>
# ----------
# parse number style datetime between (1970, 2050)
# ----------

import os
from datetime import datetime, timedelta

CONST_MIN_YEAR = 1970
CONST_MAX_YEAR = 2050

MIN = datetime(CONST_MIN_YEAR, 1, 1)
MAX = datetime(CONST_MAX_YEAR, 1, 1)
MAX_YEARS = CONST_MAX_YEAR - CONST_MIN_YEAR
MAX_DELTA = (MAX - MIN)
MAX_DAYS = MAX_DELTA.days
MAX_SECONDS = MAX_DELTA.total_seconds()


class Expression:
    def __init__(self, value, repr):
        self._repr = repr
        self._value = value

    def invoke(self):
        return eval('self.' + self._repr)

    def days_after(self, year):
        return (self._value - datetime(year, 1, 1)).days


class Result:
    def __init__(self, dt, repr):
        self._dt = dt
        self._repr = repr

    def __repr__(self):
        return self._repr

    @property
    def dt(self):
        return self._dt

    def expression(self, dt: datetime):
        return Expression(dt, self._repr)


def resolve(value):
    d = value / 60 / 60 / 24
    if d < MAX_DAYS:
        return Result(MIN + timedelta(d), 'days_after(1970) * 60 * 60 * 24')
    d = 1000
    if d < MAX_DAYS:
        return Result(MIN + timedelta(d), 'days_after(1970) * 60 * 60 * 24 * 1000')
    raise NotImplementedError
