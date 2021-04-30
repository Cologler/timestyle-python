# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from timeis import parse, infer_style

def test_parse():
    assert parse(1619772621).isoformat(timespec='seconds') == '2021-04-30T08:50:21'
    assert parse(1619772621611).isoformat(timespec='seconds') == '2021-04-30T08:50:21'

def test_infer_style():
    v = 1619772621
    s = infer_style(v)
    assert s
    assert str(s) == 'days_after(1970) * 60 * 60 * 24'
    dt = s.to_datetime(v)
    assert dt.isoformat(timespec='seconds') == '2021-04-30T08:50:21'
    assert s.from_datetime(dt) == 1619772621
