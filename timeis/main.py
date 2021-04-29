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

from .core import resolve, Result


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

    args = argv[1:]
    if not args:
        print('infer datetime from digit')
        return

    else:
        from_value = args[0]
        if from_value.isdigit():
            from_value_int = int(from_value)
        else:
            print('%r is not digit.' % from_value)
            return

        result = resolve(from_value_int)
        print('%s maybe is:' % from_value_int)
        display_result(result)
        if len(argv) == 3:
            dt = parse_datatime(argv[2])
            print(str(dt) + ' mean:')
            print('  ' + str(result.invoke(dt)))

if __name__ == '__main__':
    main()
