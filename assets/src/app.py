from flask import Flask

from src.blueprints.balances import balances
from src.blueprints.transactions import transactions
from src.blueprints.holdings import holdings

app = Flask(__name__)

app.register_blueprint(balances, url_prefix='/balances')
app.register_blueprint(transactions, url_prefix='/transactions')
app.register_blueprint(holdings, url_prefix='/holdings')
