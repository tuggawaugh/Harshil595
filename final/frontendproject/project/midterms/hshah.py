"""
"""


routes = []


def call_hshah():
    return 'Call hshah'


routes.append(dict(
    rule='/call_hshah/',
    view_func=call_hshah))


def call_hshah_2():
    return 'call_hshah_2'


routes.append(dict(
    rule='/call_hshah_2/',
    view_func=call_hshah_2,
    options=dict(methods=['GET', 'POST'])))
