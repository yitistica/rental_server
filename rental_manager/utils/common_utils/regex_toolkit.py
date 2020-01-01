import re


def _or_grouping(patterns: list, quantifier: str=None):
    expression = '(' + '|'.join(patterns) + ')'

    # parse quantifier:
    if quantifier is None:
        quantifier_suffix = ''
    else:
        quantifier_suffix = quantifier

    expression = expression + quantifier_suffix
    return expression


def retrieve(pattern: str, string: str, return_list: bool = False):
    match_dict = dict()
    iterator = re.finditer(pattern, string)
    for match in iterator:
        match_dict[match.span()] = match.group()

    if return_list:
        match_list = list(match_dict.items())

        if match_list:
            match_list.sort(key=lambda match_tuple: match_tuple[0][0])
        else:
            pass

        return match_list
    else:
        return match_dict


def search_keywords(keywords: list, string: str):
    pattern = _or_grouping(patterns=keywords)
    match_dict = retrieve(pattern, string)

    return match_dict
