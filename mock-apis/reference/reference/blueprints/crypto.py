from flask import Blueprint

# create blueprint
bp = Blueprint('stocks', __name__, url_prefix='/stocks')