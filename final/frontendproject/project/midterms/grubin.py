"""
"""


routes = []


def call_grubin():
    return 'Call grubin'


routes.append(dict(
    rule='/grubin/',
    view_func=call_grubin))


def call_grubin_2():
    return 'call_grubin_2'


routes.append(dict(
    rule='/grubin_2/',
    view_func=call_grubin_2,
    options=dict(methods=['GET', 'POST'])))
