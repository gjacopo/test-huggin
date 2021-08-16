#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Documentation of the module

The module itself should be documented:
    * overall purpose
    * useful links
    * ...
"""

import os, sys # if needed...
from collections.abc import Mapping, Sequence
from six import string_types

# import transformers
try:
    from transformers import pipeline
except:
    raise IOError('tranformers module not available')

try:
    import pandas as pd
except:
    raise IOError('pandas module not available')


class BasePipeline():
    """A generic basic class that implements whatever pipeline, as listed in the
    PIPELINES variable.
    """

    PIPE = None

    def __init__(self, *args, **kwargs):
        self.__pipe, self.__opts = None, {}
        if not args in ((),(None,)):
            self.pipe = args[0]
        else:
            self.pipe = self.PIPE
        self.opts = kwargs

    @property
    def pipe(self):
        return self.__pipe
    @pipe.setter
    def pipe(self, pipe):
        if not (pipe is None or isinstance(pipe, string_types)):
            raise TypeError("Wrong format for PIPE")
        self.__pipe = pipe

    @property
    def opts(self):
        return self.__opts
    @opts.setter
    def opts(self, opts):
        if not (opts in (None,{}) or isinstance(opts, Mapping)):
            raise TypeError("Wrong format for OPTS")
        self.__opts = opts or {}

    def __call__(self, *args, **kwargs):
        try:
            proc = pipeline(self.pipe, **self.opts)
        except:
            raise IOError("Pipeline %s not supported" % self.pipe)
        try:
            res = proc(*args, **kwargs)
        except:
            raise IOError("Pipeline process error")
        return pd.DataFrame.from_dict(
            [res] if isinstance(res, Mapping) else res,
            orient = 'columns'
            )

#note: we could have introduced configurable abstract classes

class Sentiment(BasePipeline):
    PIPE = 'sentiment-analysis'

class Summary(BasePipeline):
    PIPE = 'summarization'

class QA(BasePipeline):
    PIPE = 'question-answering'

class NER(BasePipeline):
    PIPE = 'ner'

# and also...
class Translation(BasePipeline):
    PIPE = 'translation'
    def __init__(self, *args, **kwargs):
        xx, yy = args
        super(Translation,self).__init__('translation_%s_to_%s' % (xx, yy), **kwargs)

