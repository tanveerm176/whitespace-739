import easygui
from random import random
import reader as reader
words = reader.get_csv_list( 'conspiracywords.csv' )
nouns = words[0]
verbs = words[1]
adjs = words[2]
advbs = words[3]
articles = ['a', 'an', 'the', 'one', 'at']
easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No'))
#takes list of words, returns 1 randomly chosen word
def one_of( g ):
    return g[ int( random() * len(g) ) ]
#wrapper functions for readability
def noun():
    return one_of( nouns )
def verb():
    return one_of( verbs )
def adjective():
    return one_of( adjs )
def article():
    return one_of( articles )
def adverb():
    return one_of( advbs )
def adjectives():
    if random() < .5:
        return ''
    else:
        return adjective() + ' ' + adjectives()
def adverbs():
    if random() < .5:
        return ''
    else:
        return adverb() + ' ' + adverbs();
def article_toggle():
    if random() < .5:
        return article() + ' '
    else:
        return ''
def noun_phrase():
    return article_toggle() + adjectives() + noun() + ' '
def noun_phrase_toggle():
    if random() < .5:
        return noun_phrase() + ' '
    else:
        return ''
def verb_phrase():
    return adverbs() + verb() + ' ' + noun_phrase_toggle()
def sentence():
    return noun_phrase() + verb_phrase() + 'here.'
    print sentence()
