from flask import Flask
from src.blueprints.link_accounts import link_accounts_api

app = Flask(__name__)

app.register_blueprint(link_accounts_api, url_prefix='/link-accounts')
