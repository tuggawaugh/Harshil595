"""
"""

from flask import Blueprint, render_template


mod = Blueprint('midterms', __name__)


@mod.route('/')
def hello():
    return render_template('hello.html')
#def home():
#    return 'Midterms Folder'


from .bpatel import routes as bpatel_routes
from .grubin import routes as grubin_routes
from .hshah import routes as hshah_routes
from .rwilliams import routes as rwilliams_routes


routes = (
    bpatel_routes +
    grubin_routes +
    hshah_routes +
    rwilliams_routes )

for r in routes:
    mod.add_url_rule(
        r['rule'],
        endpoint=r.get('endpoint', None),
        view_func=r['view_func'],
        **r.get('options', {}))





