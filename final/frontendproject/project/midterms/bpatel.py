"""
"""


routes = []


def call_bpatel():
    return 'Call bpatel'


routes.append(dict(
    rule='/call_bpatel/',
    view_func=call_bpatel))


def call_bpatel_2():
    return 'call_bpatel_2'


routes.append(dict(
    rule='/call_bpatel_2/',
    view_func=call_bpatel_2,
    options=dict(methods=['GET', 'POST'])))
