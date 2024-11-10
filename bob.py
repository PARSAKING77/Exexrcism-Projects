def response(hey_bob):

    trimmed_input = hey_bob.strip()
    
    if trimmed_input == "":
        return "Fine. Be that way!"
    
    if trimmed_input.isupper():

        if trimmed_input.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    
    if trimmed_input.endswith('?'):
        return "Sure."
    
    return "Whatever."