#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A wrapper for entity recognition to KNIME
"""

from .pipes import NER

class NERWraper(NER):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(NER,self).__call__(*args, **kwargs)

if __name__ == "__main__":
    ner = NERWraper()
    output_table_1 = ner(input_table_1)
