def is_pangram(sentence):

    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    sentence_set = set(sentence.lower())
    
    return alphabet_set <= sentence_set
