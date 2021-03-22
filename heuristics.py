from filter_options import favored_keywords, blocked_keywords

always_true = lambda _ : True
always_false = lambda _: False

# profile passed in as a dictionary
def filter_blocked(profile):
    compl_str = cat_dict(profile)

    for blocked in blocked_keywords:
        if blocked.lower() in compl_str:
            return False

    return True


# profile passed in as a dictionary
def favored_only(profile):
    compl_str = cat_dict(profile)
    
    for favored in favored_keywords:
        if favored.lower() in compl_str:
            return True

    return False

# cat dict entries, returns string of all dictionary entries concatenated and lower cased
def cat_dict(profile):
    compl_str = ""
    for s in profile.values:
        compl_str += s + ' '
    compl_str.lower()
    return compl_str

