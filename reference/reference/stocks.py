from flask import (Blueprint, jsonify)
from twelvedata import TDClient
import os


td = TDClient(apikey=os.environ.get('TD_API_KEY'))

bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@bp.route('/test', methods=('GET', 'POST'))
def test():
    ts = td.time_series(
    symbol="AAPL, TSLA, IBM, GME",
    outputsize=1,
    interval="1min"
)   
    return jsonify(ts.as_json())
