def is_tachycardic(s):
    s = s.lower()
    target = "tachycardic"
    if target in s:
        return True
    import re
    letters_only = re.search(r'[a-z]+', s)
    s = letters_only.group(0)
    from difflib import SequenceMatcher as SM
    match_ratio = SM(None, s, target).ratio()
    number_of_matched_letters = match_ratio * (len(s) + len(target)) / 2
    print(number_of_matched_letters)
    return number_of_matched_letters >= (len(target) - 2)

# print(is_tachycardic("tachycard"))
