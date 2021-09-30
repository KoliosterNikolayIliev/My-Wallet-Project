from flask import (
    Blueprint
)

bp = Blueprint('crypto', __name__, url_prefix='/crypto')

@bp.route('/test', methods=('GET', 'POST'))
def test():
    return 'crypto test'
