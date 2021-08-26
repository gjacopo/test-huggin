#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script for question_answering in KNIME
"""

from test_huggin.pipes import QA

try: # set to run with KNIME
    __name__ # assert('__name__' in locals() or '__name__' in globals())
except NameError: # AssertionError:
    __name__ = "__main__"

class KQA(QA):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['context'][0], arg['question'][0]
        except:
            args = (arg,)
        else:
            args = ()
            kwargs.update(zip(['context','question'], arg))
        return super(KQA,self).__call__(*args, **kwargs)

if __name__ == "__main__":
    qa = KQA()
    output_table_1 = qa(input_table_1)
