from flask import Blueprint, jsonify

# create blueprint
bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@bp.route('/prices', methods=['GET'])
def prices():
    test_data = {
        'AAPL': 138.13,
        'MSFT': 281.24,
        'PLTR': 23.20,
        'GOOGL': 2654.24,
        'AMZN': 3185.66,
        'MRNA': 325.30,
        'TSLA': 782.06,
        'AMD': 100.00,
    }
    return jsonify(test_data)