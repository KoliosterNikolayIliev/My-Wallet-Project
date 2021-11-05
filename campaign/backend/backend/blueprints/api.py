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
    return jsonify({'count': int(getLists()) + 324})

@bp.route("/save-form-data", methods=["POST"])
def save_form_data():
    author = request.json['author']
    quiz = request.json['quiz']
    data = {
        "author": author,
        "What do you hope Trivial will help you with? (Select all that apply)": ', '.join(quiz['What do you hope Trivial will help you with? (Select all that apply)']),
        "What do you use to solve this problem now? (Select only one option)": quiz['What do you use to solve this problem now? (Select only one option)'][0],
        "Please list all of the investment platforms you use today?": quiz['Please list all of the investment platforms you use today?'][0],
    }

    with open('data.csv', 'a+', encoding='UTF8') as f:
        writer = csv.DictWriter(f, ["author", "What do you hope Trivial will help you with? (Select all that apply)", "What do you use to solve this problem now? (Select only one option)", "Please list all of the investment platforms you use today?"])
        if os.stat('data.csv').st_size == 0:
            writer.writeheader()
        writer.writerow(data)

    return jsonify({'status': 'success'})