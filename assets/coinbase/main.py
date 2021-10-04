import cbpro
from flask import Flask, jsonify

# Second API credentials for the accounts:
api_secret_acc = 'F2xOifdoBXgXu+1CWmlBXO4Y0VM7XuWIiJMPcA55dxY0ddMcBOywpDmbx7KlAJ/kgXkXKRGvvM9AyZsgEuCvHQ=='
api_key_acc = '96c453261680c5edff567425d54c5014'
api_pass_acc = 'vl8hxvmfhz'

URL = 'https://api-public.sandbox.pro.coinbase.com'
API_KEY = api_key_acc
API_SECRET = api_secret_acc
API_PASS = api_pass_acc

app = Flask(__name__)

""" Authenticate the client """
client = cbpro.AuthenticatedClient(
    key=API_KEY,
    b64secret=API_SECRET,
    passphrase=API_PASS,
    api_url=URL
)


all_clients = client.get_accounts()  # method to check all existing clients

"""
Our test client is with ID "b0f26bb3-17ed-4281-8cad-9068ea09a96c"
"""
account_id = 'b0f26bb3-17ed-4281-8cad-9068ea09a96c'

""" Use this endpoint when you know the account_id. """
client_data = client.get_account(account_id)

# @app.route('/account', methods=['GET'])
# def get():
#     return jsonify({"Client data": client_data})


client_history = client.get_account_history(account_id)
current_holdings = client.get_account_holds(account_id)

client_history_list = []

for each in client_history:
    client_history_list.append(each)


@app.route('/')
def index():
    return "Welcome"

""" Get all orders from particular clieent """
@app.route('/orders', methods=['GET'])
def get():
    return jsonify({"Client orders": client_history_list})


""" Get all orders by id """
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return jsonify({"Client order": client_history_list[order_id - 1]})


if __name__ == '__main__':
    app.run(debug=True)
