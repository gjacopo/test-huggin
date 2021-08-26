#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script for sentiment analysis in KNIME
"""

from test_huggin.pipes import Sentiment

try: # set to run with KNIME
    __name__ # assert('__name__' in locals() or '__name__' in globals())
except NameError: # AssertionError:
    __name__ = "__main__"

class KSentiment(Sentiment):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(KSentiment,self).__call__(*args, **kwargs)

if __name__ == "__main__":
    sentiment = KSentiment()
    output_table_1 = sentiment(input_table_1)
