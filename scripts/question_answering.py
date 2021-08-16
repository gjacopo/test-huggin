#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A wrapper for question_answering to KNIME
"""

from .pipes import QA

class QAWrapper(QA):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['context'][0], arg['question'][0]
        except:
            args = (arg,)
        else:
            args = ()
            kwargs.update(zip(['context','question'], arg))
        return super(QA,self).__call__(*args, **kwargs)

if __name__ == "__main__":
    qa = QAWrapper()
    output_table_1 = qa(input_table_1)
