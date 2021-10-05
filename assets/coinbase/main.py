import cbpro
from flask import Flask, jsonify

app = Flask(__name__)

""" Hardcoded 4 variables that should come from the Admin module """
account_id = 'b0f26bb3-17ed-4281-8cad-9068ea09a96c'
api_secret_acc = 'F2xOifdoBXgXu+1CWmlBXO4Y0VM7XuWIiJMPcA55dxY0ddMcBOywpDmbx7KlAJ/kgXkXKRGvvM9AyZsgEuCvHQ=='
api_key_acc = '96c453261680c5edff567425d54c5014'
api_pass_acc = 'vl8hxvmfhz'

""" The URL path is currently leading to the test enviroement.
Once the app is ready, it needs to be changed to:
'https://api-public.pro.coinbase.com' """
URL = 'https://api-public.sandbox.pro.coinbase.com'
API_KEY = api_key_acc
API_SECRET = api_secret_acc
API_PASS = api_pass_acc

""" Authenticate the client via the cbpro library"""
client = cbpro.AuthenticatedClient(
    key=API_KEY,
    b64secret=API_SECRET,
    passphrase=API_PASS,
    api_url=URL
)

client_data = client.get_account(account_id)

""" Get client's current balance """


@app.route('/balances', methods=['GET'])
def get_account():
    return jsonify({"Client data": client_data})


""" Get client's all transactions """
client_history = client.get_account_history(account_id)

client_history_list = []
for each in client_history:
    client_history_list.append(each)


@app.route('/transactions', methods=['GET'])
def get_orders():
    return jsonify({"Client orders": client_history_list})


if __name__ == '__main__':
    app.run(debug=True)
