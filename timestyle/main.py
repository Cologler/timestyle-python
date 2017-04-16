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

from core import enumerate_results, Result


def display_result(r: Result):
    msg = '  {dt} (by {repr})'.format(dt=r.dt, repr=repr(r))
    print(msg)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        if len(argv) == 2:
            intvalue = int(argv[1])
            print('possible:')
            for r in enumerate_results(intvalue):
                display_result(r)
            print('end.')
    except Exception:
        traceback.print_exc()
        input()

if __name__ == '__main__':
    main()
