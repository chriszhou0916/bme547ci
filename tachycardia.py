def is_tachycardic(s):
    # Exact case
    s = s.lower()
    target = "tachycardic"
    if target in s:
        return True
    # Fuzzy case
    import re
    # Used regular expression to extract the word, only works with single word
    letters_only = re.search(r'[a-z]+', s)
    s = letters_only.group(0)
    # Referenced online resource for fuzzy string matching
    # https://stackoverflow.com/questions/10383044/fuzzy-string-comparison
    from difflib import SequenceMatcher as SeqMatch
    match_ratio = SeqMatch(None, s, target).ratio()  # percent matches between two words
    # Converts percent match to absolute number of matches
    number_of_matched_letters = match_ratio * (len(s) + len(target)) / 2
    # Only returns true if number of matches is no less than 2 of total length of target
    return number_of_matched_letters >= (len(target) - 2)
