from flask import (
    Blueprint
)

bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@bp.route('/test', methods=('GET', 'POST'))
def test():
    return 'stocks test'
