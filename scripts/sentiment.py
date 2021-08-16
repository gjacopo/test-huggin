#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A wrapper for sentiment analysis to KNIME
"""

from test_huggin.pipes import Sentiment

class SentimentWrapper(Sentiment):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(Sentiment,self).__call__(*args, **kwargs)

if __name__ == "__main__":
    sentiment = SentimentWrapper()
    output_table_1 = sentiment(input_table_1)
