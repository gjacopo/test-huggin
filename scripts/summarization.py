#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A wrapper for summarization to be launched through KNIME
"""

from .pipes import Summary

class SummaryWrapper(Summary):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(WrapperSummary,self).__call__(*args, **kwargs)

if __name__ == "__main__":
    summary = SummaryWrapper()
    output_table_1 = summary(input_table_1)