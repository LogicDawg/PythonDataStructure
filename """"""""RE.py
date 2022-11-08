def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ""
    for letter in phrase:
        if letter == to_swap:
            if islower(to_swap) == True:
                if isupper(letter) == True:
                    new_str += letter.lower()
                elif islower(to_swap) == False:
                    new_str += letter
    return new_str
