#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script for summarization in KNIME
"""

from test_huggin.pipes import Summary

try: # set to run with KNIME
    __name__ # assert('__name__' in locals() or '__name__' in globals())
except NameError: # AssertionError:
    __name__ = "__main__"

class KSummary(Summary):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(KSummary,self).__call__(*args, **kwargs)

if __name__ == "__main__":
    summary = KSummary()
    output_table_1 = summary(input_table_1)
