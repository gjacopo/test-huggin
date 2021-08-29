#!/usr/bin/env python3
# note the line above is useful to launch the script from the command line, e.g. using
# python -m ...
"""
Document the script, for instance:
Parse in the KNIME output an article table from the main fields of an online article parsed through
the KNIME input.
"""

from six import string_types
from collections.abc import Sequence
import pandas as pd

try: 
    __name__ 
except NameError:
    __name__ = "__main__"

try:
    from newspaper import Article
except ImportError:
    raise ImportError ('package newspaper not available')

DEF_URLS = ['http', 'https', 'ftp']
DEF_FIELDS = [ 'authors', 'publish_date', 'text','top_image', 'keywords', 'summary']

def art_to_table(url, fields = None):
    """Create an article table from the main fields of an online article parsed through its URL. 
    
    >>> table = art_to_table(url, fields = None)
    
    Arguments
    ---------
    url : str
        URL of the online article; should start with any string from `DEF_URLS`.
    fields : list[str]
        fields of the article to parse in the output table; when `None`, set to the default
        list of fields: `DEF_FIELDS`.
        
    Returns
    -------
    table: pd.DataFrame
        A data frame with the `fields` of the article as columns.
    """
    try: # that... or use typing of functions enabled by Python 3: -->
        assert(isinstance(url,string_types))
    except AssertionError:
        raise TypeError('wrong type for URL')
    try: # catching other errors... or not
        assert(any([isinstance(url.startswith(pre)) for pre in DEF_URLS))
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
            d.update({f: [getattr(article, f)}])
        except:
            raise IOError('Unknown field %s of article' % f)
    return pd.DataFrame(d)

if __name__ == "__main__":
    output_table_1 = art_to_table(input_table_1['text'][0])
