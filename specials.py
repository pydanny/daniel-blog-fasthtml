from collections import OrderedDict
import re
from functools import lru_cache

from fasthtml.common import *
from contents import *

__all__ = ['word_counter',]


@lru_cache
def word_counter(limit=None):
    """Counts words in text"""

    # Get all the posts and put their content in a single string
    text = '/n'.join([x['content'] for x in list_posts(content=True)])


    word_ct = {}
    for word in re.findall(r'\w+', text.lower()):
        word_ct[word] = word_ct.get(word, 0) + 1
    
    # Sort the word_counts dictionary by value (count) in descending order
    sorted_word_counts = sorted(word_ct.items(), key=lambda x: x[1], reverse=True)

    # Remove stopwords if there are any
    stopwords="the,to,in,of,for,a,an,with,on,at,by,from,that,this,who,and,whose,whom,where,when,why,how,what,whom,is"
    stopwords+="was,my,you,we,be,are,but,have,so,https,com,can,do,me,about,up,more"
    sorted_word_counts = [(k, v) for k, v in sorted_word_counts if k not in stopwords]

    if limit is not None:
        sorted_word_counts = sorted_word_counts[:limit]    
    
    # Create an OrderedDict from the sorted list
    return OrderedDict(sorted_word_counts)