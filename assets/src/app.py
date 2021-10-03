from flask import Flask

from src.blueprints.balances import balances
from src.blueprints.link_accounts import link_accounts
from src.blueprints.transactions import transactions

app = Flask(__name__)

app.register_blueprint(link_accounts, url_prefix='/link-accounts')
app.register_blueprint(balances, url_prefix='/balances')
app.register_blueprint(transactions, url_prefix='/transactions')
