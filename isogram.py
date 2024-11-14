def is_isogram(string):
    cleaned_word = string.replace(" ", "").replace("-", "").lower()
    
    letter_set = set(cleaned_word)
    
    return len(letter_set) == len(cleaned_word)

