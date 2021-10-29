from flask import Blueprint, jsonify, request
from flask_cors import CORS
import mailchimp_marketing
import os, csv

bp = Blueprint('api', __name__)
CORS(bp)

client = mailchimp_marketing.Client()
client.set_config({
    "api_key": os.environ.get("MAILCHIMP_KEY"),
    "server": "us5"
})

def getLists():
    lists = client.lists.get_all_lists()
    return lists["lists"][0]["stats"]["member_count_since_send"]

@bp.route("/subscribers", methods=["GET"])
def get_subscribers():
    return jsonify({'count': getLists()})

@bp.route("/save-form-data", methods=["POST"])
def save_form_data():
    author = request.json['author']
    quiz = request.json['quiz']
    data = {
        "author": author,
        "quiz": quiz
    }

    with open('data.csv', 'a+', encoding='UTF8') as f:
        writer = csv.DictWriter(f, ["author", "quiz"])
        if os.stat('data.csv').st_size == 0:
            writer.writeheader()
        writer.writerow(data)

    return jsonify({'status': 'success'})