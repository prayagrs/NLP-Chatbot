
from nltk import *

def getResponse(user_query):
    text = user_query
    sents = word_tokenize(text)
    tagged_token = pos_tag(sents)

    for words in tagged_token:
        if(words[1] == "JJ"):
            return "Are you sure you want to eat",words[0],"?"