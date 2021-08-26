#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Documentation of the module

The module itself should be documented:
    * overall purpose
    * useful links
    * ...
"""

from .pipes import Summary, Sentiment, QA, NER

class KSummary(Summary):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(KSummary,self).__call__(*args, **kwargs)

class KSentiment(Sentiment):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(KSentiment,self).__call__(*args, **kwargs)

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

class KNER(NER):
    def __call__(self, arg, **kwargs):
        try:
            arg = arg['text'][0]
        except:
            pass
        args = (arg,)
        return super(KNER,self).__call__(*args, **kwargs)

