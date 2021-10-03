from flask import Flask
from src.blueprints.link_accounts import link_accounts

app = Flask(__name__)

app.register_blueprint(link_accounts, url_prefix='/link-accounts')
