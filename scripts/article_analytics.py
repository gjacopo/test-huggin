#!/usr/bin/env python3
# note the line above is useful to launch the script from the command line, e.g. using
# python -m ...
"""
Document the script
"""

from six import string_types
from collections.abc import Sequence
import pandas as pd

try:
    from newspaper import Article
except ImportError:
    raise ImportError ('package newspaper not available')

URL_SITES = ['http', 'https', 'ftp']
DEF_FIELDS = [ 'authors', 'publish_date', 'text','top_image', 'keywords', 'summary']

def dummy(url, fields = None):
    try: # that... or use typing of functions enabled by Python 3: -->
        assert(isinstance(url,string_types))
    except AssertionError:
        raise TypeError('wrong type for URL')
    try: # catching other errors... or not
        assert(any([isinstance(url.startswith(pre)) for pre in URL_SITES))
    except AssertionError:
        raise IOError('URL type not recognised')
    try:
        assert (fields is None or isinstance(fields, Sequence))
    except:
        raise TypeError('wrong type for fields')
    else:
        if fields is None:
            fields = DEF_FIELDS
    # catch errors
    try:
        article = Article(url)
    except:
        raise IOError('Error creating Article instance from URL')
    try:
        article.download()
        article.parse()
        article.nlp()
    except:
        raise IOError('Error processing article')
    d = {}
    for f in fields:
        try:
            d.update({f: getattr(article, f)})
        except:
            raise IOError('Unknown field %s of article' % f)
    return pd.DataFrame(d)

if __name__ == "__main__":
    # please check why https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    output_table_1 = dummy(input_table_1['text'][0])
