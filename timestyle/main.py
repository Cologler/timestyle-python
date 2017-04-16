#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
import sys
import traceback
import re
from datetime import datetime

from core import resolve, Result


def parse_datatime(value: str):
    m = re.match('^(\\d{4})-(\\d{1,2})-(\\d{1,2})$', value)
    if m:
        return datetime(*[int(z) for z in m.groups()])
    raise NotImplementedError


def display_result(r: Result):
    msg = '  {dt} (by {repr})'.format(dt=r.dt, repr=repr(r))
    print(msg)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        if len(argv) > 1:
            intvalue = int(argv[1])
            print('possible:')
            result = resolve(intvalue)
            display_result(result)
            if len(argv) == 3:
                dt = parse_datatime(argv[2])
                print(str(dt) + ' mean:')
                print('  ' + str(result.expression(dt).invoke()))
    except Exception:
        traceback.print_exc()
        input()

if __name__ == '__main__':
    main()
