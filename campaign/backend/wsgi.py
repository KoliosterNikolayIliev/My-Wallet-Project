from flask import Flask, jsonify
import mailchimp_marketing
import os

app = Flask(__name__)

client = mailchimp_marketing.Client()
client.set_config({
    "api_key": os.environ.get("MAILCHIMP_KEY"),
    "server": "us5"
})

def getLists():
    lists = client.lists.get_all_lists()
    return lists["lists"][0]["stats"]["member_count_since_send"]

@app.route("/subscribers")
def get_subscribers():
    return jsonify({'count': getLists()})