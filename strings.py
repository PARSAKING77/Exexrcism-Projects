"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended."""
    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    return ' :: '.join([prefix] + words_with_prefix)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    if word.endswith('ness'):
        root_word = word[:-5]  # Remove 'ness'
        if len(root_word) > 1 and root_word[-1] == 'y' and root_word[-2] not in 'aeiou':
            # If it ends with consonant + y, change 'y' to 'i'
            root_word = root_word[:-1] + 'y'
        return root_word
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()  # Split the sentence into words
    adjective = words[index]  # Get the word at the specified index
    return adjective + 'en'  # Add 'en' to the adjective to convert it to a verb