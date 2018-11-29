"""
"""


routes = []


def call_rwilliams():
    return 'Call rwilliams'


routes.append(dict(
    rule='/call_rwilliams/',
    view_func=call_rwilliams))


def call_rwilliams_2():
    return 'call_rwilliams_2'


routes.append(dict(
    rule='/call_rwilliams_2/',
    view_func=call_rwilliams_2,
    options=dict(methods=['GET', 'POST'])))
