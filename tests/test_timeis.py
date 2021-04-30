# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from timeis import parse

def test_parse():
    assert parse(1619772621).isoformat().startswith('2021-04-30T08:50:21')
    assert parse(1619772621611).isoformat().startswith('2021-04-30T08:50:21')
